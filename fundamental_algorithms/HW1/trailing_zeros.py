def trailing_zeros_string_conversion(n):
    int_string = str(n)
    length = len(int_string) - 1
    zero_count = 0
    s1 = ""
    while length >= 0:
        s1 = s1 + int_string[length]
        length = length - 1
    for character in s1:
        if character == "0":
            zero_count += 1
        else:
            break
    return zero_count


# print(trailing_zeros_string_conversion(0))
# print(trailing_zeros_string_conversion(2))
# print(trailing_zeros_string_conversion(50))
# print(trailing_zeros_string_conversion(1200))


def trailing_zeros(n):
    count = 0
    while n != 0:
        # invariant:
        # n >= 0
        temp = n % 10
        if temp == 0:
            count += 1
        else:
            break
        n /= 10
    return count


# int main(){
#   int a=2000,count=0,temp;
#   while(a!=0)
#   {
#     temp=a%10;
#     if(temp==0) count++
#     else break;
#     a/=10;
#   }
#   printf("%d",count);
# }

print(trailing_zeros(0))
print(trailing_zeros(2))
print(trailing_zeros(21))
print(trailing_zeros(5000))
print(trailing_zeros(1200))
