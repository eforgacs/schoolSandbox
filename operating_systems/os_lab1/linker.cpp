#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>


using namespace std;
#define BUFFER_SIZE 1024
#define MEMORY_SIZE 512
#define ERROR_BUFFER 256
int line_number = 0;
int line_offset = 0;
bool afterDef = true;

class Symbol {
public:
    string symName;
    bool duplicated;
    bool inUseList;
    bool used;
    int module;
    int value;


    Symbol() {
        symName = "";
        duplicated = false;
        inUseList = true;
        used = false;
        module = 0;
        value = 0;
    }
};

class Module {
public:
    int moduleNumber{};
    int instructionNumber{};
    int base{};
    vector<Symbol *> symbolTable;

    int getInstructionNumber() const {
        return instructionNumber;
    }

    void setInstructionNumber(int instruction_value) {
        Module::instructionNumber = instruction_value;
    }

    int getModuleNumber() const {
        return moduleNumber;
    }

    void setModuleNumber(int module_value) {
        Module::moduleNumber = module_value;
    }

    int getBase() const {
        return base;
    }

    void setBase(int base_value) {
        Module::base = base_value;
    }

    const vector<Symbol *> &getSymbolTable() const {
        return symbolTable;
    }

    void setSymbolTable(const vector<Symbol *> &table) {
        Module::symbolTable = table;
    }
};

void __parseerror(int errcode) {
    const char *errstr[] = {
            "NUM_EXPECTED", // Number expect, anything >= 2^30 is not a number either
            "SYM_EXPECTED", // Symbol Expected
            "ADDR_EXPECTED", // Addressing Expected which is A/E/I/R
            "SYM_TOO_LONG", // Symbol Name is too long
            "TOO_MANY_DEF_IN_MODULE", // > 16
            "TOO_MANY_USE_IN_MODULE", // > 16
            "TOO_MANY_INSTR",           // total num_instr exceeds memory size (512)
    };
    printf("Parse Error line %d offset %d: %s\n", line_number, line_offset, errstr[errcode]);
}

void initializePass1(vector<Symbol *> &defList, vector<Symbol *> &symbolTable);


void initializePass2(vector<Symbol> &useList, vector<Symbol *> &symbolTable, int &currentBase);

char *getToken(ifstream &inputStream) {
    static bool eol = true;
    static char buffer[BUFFER_SIZE];
    static int length;
    static char *strtokPtr;
    static char *token;

    while (true) {
        if (eol) {
            if (inputStream.eof()) {
                return nullptr;
            }
            if (!inputStream.getline(buffer, BUFFER_SIZE)) {
                line_offset = 1 + length;
                return nullptr;
            } else {
                eol = false;
                length = int(strlen(buffer));
                strtokPtr = buffer;
                line_number++;
            }
        }
        token = strtok(strtokPtr, " \t\n");
        strtokPtr = nullptr;
        if (token == nullptr) {
            eol = true;
            continue;
        }
        line_offset = token - buffer + 1;
        return token;
    }
}

int readInt(ifstream &inputStream) {
    char *tok = getToken(inputStream);
    if (tok != nullptr) {
        for (int i = 0; i < strlen(tok); i++) {
            if (!isdigit(tok[i])) {
                __parseerror(0);
                exit(1);
            }
        }
        return strtol(tok, nullptr, 10);
    }
    if (afterDef) {
        __parseerror(0);
        exit(EXIT_FAILURE);
    } else {
        return -1;
    }
}

char *readSymbol(ifstream &inputStream) {
    char *tok = getToken(inputStream);
    if (tok == nullptr || isdigit(tok[0]) || !isalnum(tok[0])) {
        __parseerror(1);
        exit(1);
    } else if (strlen(tok) > 16) {
        __parseerror(3);
        exit(1);
    }
    return tok;
}

char readIAER(ifstream &inputStream) {
    char *tok = getToken(inputStream);
    if (tok == nullptr || *tok != 'I' && *tok != 'A' && *tok != 'E' && *tok != 'R') {
        __parseerror(2);
        exit(1);
    }
    return *tok;
}

Module module;

void Pass1(ifstream &inputStream) {
    vector<Symbol *> defList;
    vector<Symbol *> symbolTable;
    initializePass1(defList, symbolTable);
    while (!inputStream.eof()) {
        int moduleNum = module.getModuleNumber();
        int instructionNumber = module.getInstructionNumber();
        afterDef = false;
        int defcount = readInt(inputStream);
        if (defcount == -1) {
            break;
        }
        if (defcount > 16) {
            __parseerror(4);
            exit(1);
        }
        for (int i = 0; i < defcount; i++) {
            char *defSym = readSymbol(inputStream);
            afterDef = true;
            int val = readInt(inputStream);
            bool inTable = false;
            Symbol *newSym = nullptr;
            for (auto &j : symbolTable) {
                if (j->symName == defSym) {
                    j->duplicated = true;
                    newSym = j;
                    inTable = true;
                    break;
                }
            }
            if (!inTable) {
                newSym = new Symbol();
                newSym->symName = defSym;
                newSym->value = val + instructionNumber;
                newSym->module = moduleNum;
                symbolTable.push_back(newSym);

            }
            defList.push_back(newSym);
        }

        afterDef = true;
        int use_count = readInt(inputStream);
        if (use_count == -1) {
            break;
        }
        if (use_count > 16) {
            __parseerror(5);
            exit(1);
        }
        for (int i = 0; i < use_count; i++) {
            readSymbol(inputStream);
        }

        afterDef = true;
        int instructionCount = readInt(inputStream);
        if (instructionCount == -1) {
            break;
        }
        if (instructionCount + instructionNumber >= MEMORY_SIZE) {
            __parseerror(6);
            exit(1);
        }
        for (int i = 0; i < instructionCount; i++) {
            readIAER(inputStream);
            afterDef = true;
            readInt(inputStream);
        }
        for (auto &i : defList) {
            if (i->value >= instructionNumber + instructionCount) {
                string sym = i->symName;
                printf("Warning: Module %d: %s too big %d (max=%d) assume zero relative\n", moduleNum,
                       i->symName.c_str(), i->value - instructionNumber, instructionCount - 1);
                i->value = instructionNumber;
            }
        }
        module.setModuleNumber(moduleNum + 1);
        module.setInstructionNumber(instructionNumber + instructionCount);
        module.setSymbolTable(symbolTable);
        defList.clear();
    }

}

void initializePass1(vector<Symbol *> &defList, vector<Symbol *> &symbolTable) {
    symbolTable = module.getSymbolTable();
    module.setInstructionNumber(0);
    module.setModuleNumber(1);
}

void printSymbolTable() {
    vector<Symbol *> symbolTable = module.getSymbolTable();
    cout << "Symbol Table" << endl;
    for (auto &i : symbolTable) {
        cout << i->symName << "=" << i->value;
        if (i->duplicated) {
            cout << " Error: This variable is multiple times defined; first value used";
        }
        cout << endl;
    }
}

string handleA(char *buffer, int opcode, int operand, int &op) {
    string error;
    if (opcode >= 10) {
        error = std::to_string(sprintf(buffer, " Error: Illegal opcode; treated as 9999"));
        op = 9999;
    } else if (operand >= MEMORY_SIZE) {
        error = std::to_string(sprintf(buffer, " Error: Absolute address exceeds machine size; zero used"));
        op = opcode * 1000;
    }
    return error;
}

string handleR(char *buffer, int opcode, int operand, int &op, int currentBase, int instructionCount) {
    string error;
    if (opcode >= 10) {
        error = std::to_string(sprintf(buffer, " Error: Illegal opcode; treated as 9999"));
        op = 9999;
    } else {
        if (operand > instructionCount - 1) {
            error = std::to_string(sprintf(buffer, " Error: Relative address exceeds module size; zero used"));
            op = op - operand;
        }
        if (module.moduleNumber != 0) {
            op = op + currentBase;
        }
    }
    return error;
}

string
handleE(char *buffer, int opcode, int operand, int &op, vector<Symbol> &useList, const vector<Symbol *> &symbolTable) {
    string error;
    if (opcode >= 10) {
        error = std::to_string(sprintf(buffer, " Error: Illegal opcode; treated as 9999"));
        op = 9999;
    } else {
        if (operand >= useList.size()) {
            error = std::to_string(
                    sprintf(buffer, " Error: External address exceeds length of uselist; treated as immediate"));
        } else {
            string usedSym = useList[operand].symName;
            bool defined = false;
            for (auto &i : symbolTable) {
                if (usedSym == i->symName) {
                    defined = true;
                    op = opcode * 1000 + i->value;
                    i->used = true;
                    break;
                }
            }
            useList[operand].inUseList = true;
            if (!defined) {
                error = std::to_string(sprintf(buffer, " Error: %s is not defined; zero used", usedSym.c_str()));
                op = opcode * 1000;
            }
        }
    }
    return error;
}

string handleI(char *buffer, int opcode, int &op) {
    string error;
    if (opcode >= 10) {
        error = std::to_string(sprintf(buffer, " Error: Illegal immediate value; treated as 9999"));
        op = 9999;
    }
    return error;
}

void Pass2(ifstream &inputStream) {
    vector<Symbol> useList;
    vector<Symbol *> symbolTable;
    int currentBase;
    initializePass2(useList, symbolTable, currentBase);

    while (!inputStream.eof()) {
        int moduleNum = module.getModuleNumber();
        int instNum;
        afterDef = false;
        int definition_count = readInt(inputStream);
        if (definition_count == -1) {
            break;
        }
        for (int i = 0; i < definition_count; i++) {
            readSymbol(inputStream);
            afterDef = true;
            readInt(inputStream);
        }

        afterDef = true;
        int use_count = readInt(inputStream);
        if (use_count == -1) {
            break;
        }
        for (int i = 0; i < use_count; i++) {
            char *useSym = readSymbol(inputStream);
            Symbol newSym;
            newSym.symName = useSym;
            newSym.module = moduleNum;
            newSym.inUseList = false;
            useList.push_back(newSym);
        }

        afterDef = true;
        int instance_count = readInt(inputStream);
        if (instance_count == -1) {
            break;
        }
        char buffer[ERROR_BUFFER] = "";
        string error;
        for (int i = 0; i < instance_count; i++) {
            char address_mode = readIAER(inputStream);
            module.instructionNumber = module.instructionNumber + 1;
            instNum = module.instructionNumber;
            afterDef = true;
            int op = readInt(inputStream);
            int opcode = op / 1000;
            int operand = op % 1000;
            buffer[0] = '\0';
            switch (address_mode) {
                case 'A':
                    handleA(buffer, opcode, operand, op);
                    break;
                case 'R':
                    handleR(buffer, opcode, operand, op, currentBase, instance_count);
                    break;
                case 'E':
                    handleE(buffer, opcode, operand, op, useList, symbolTable);
                    break;
                case 'I':
                    handleI(buffer, opcode, op);
                    break;
                default:
                    break;
            }
            cout << setfill('0') << setw(3) << instNum << ": " << setfill('0') << setw(4) << op;
            if (strlen(buffer) > 0) {
                cout << buffer;
            }
            printf("\n");
        }
        for (auto &i : useList) {
            if (!i.inUseList) {
                printf("Warning: Module %d: %s appeared in the uselist but was not actually used\n", moduleNum,
                       i.symName.c_str());
            }
        }
        module.setModuleNumber(moduleNum + 1);
        currentBase += instance_count;
        module.setBase(currentBase);
        useList.clear();
    }
}

void initializePass2(vector<Symbol> &useList, vector<Symbol *> &symbolTable, int &currentBase) {
    symbolTable = module.getSymbolTable();
    currentBase = module.getBase();
    module.setInstructionNumber(-1);
    module.setModuleNumber(1);
    module.setBase(0);
}

void printWarning() {
    vector<Symbol *> symbolTable = module.getSymbolTable();
    printf("\n");
    for (auto &i : symbolTable) {
        if (!i->used) {
            printf("Warning: Module %d: %s was defined but never used\n", i->module,
                   i->symName.c_str());
        }
    }
    printf("\n");
}

int main(int argc, char *argv[]) {
    ifstream input_stream;
    input_stream.open(argv[1]);
    if (!input_stream.is_open() || argc > 2) {
        cout << "Invalid input file <" << argv[1] << ">" << endl;
        return 0;
    } else if (argc == 1) {
        cout << "Invalid arguments provided " << endl;
        return 0;
    }
    Pass1(input_stream);
    printSymbolTable();
    input_stream.close();
    input_stream.open(argv[1]);
    printf("\nMemory Map\n");
    Pass2(input_stream);
    printWarning();
    input_stream.close();
    return 0;
}