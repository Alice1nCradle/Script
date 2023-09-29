#种子数组字符串
# seed='dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87'
#种子数组字符串的十六进制列表
seed=[0x64, 0x73, 0x66, 0x64, 0x3b, 0x6b, 0x66, 0x6f,
      0x41, 0x2c, 0x2e, 0x69, 0x79, 0x65, 0x77, 0x72,
      0x6b, 0x6c, 0x64, 0x4a, 0x4b, 0x44, 0x48, 0x53,
      0x55, 0x42, 0x73, 0x67, 0x76, 0x63, 0x61, 0x36,
      0x39, 0x38, 0x33, 0x34, 0x6e, 0x63, 0x78, 0x76,
      0x39, 0x38, 0x37, 0x33, 0x32, 0x35, 0x34, 0x6b,
      0x3b, 0x66, 0x67, 0x38, 0x37]

# 密文
c='094F5A0F0A0D1805103B0B3D143117183B720438350A45550967674D1E064F2969784440455A460F1A1B'

# 函数名：get_seed
# 参数：数值型的字符串
# 功能：将字符串转换为十进制数
# 返回值：返回转换后的十进制数
def get_seed(str0):
    #进制转换并返回结果
    return int(str0[0])*10+int(str0[1])

#主函数入口
if __name__ == '__main__':
    #读取密文加密种子在列表中的下表
    int_seed=get_seed(c[0:2])
    #打印下标，可删除
    print(int_seed)
    # 获取密文长度
    int_c_len=len(c)
    #实际待解密内容开始位置
    int_k=2
    #存储解密结果的变量
    result=''
    # 未到密文长度末尾，未完成加密内容解密，继续循环
    while int_k<int_c_len:
        #采用加密种子与待解密内容的十六进制进行异或，得到明文，存入result变量中
        result+=chr(seed[int_seed]^int(c[int_k:int_k+2],base=16))
        #加密种子后移一位
        int_seed+=1
        #记录下一个待解密内容的值
        int_k += 2
        #判断是否到加密种子末尾
        if int_seed>52:
            #到达加密种子末尾，从头开始
            int_seed=int_seed%53
    #输出解密结果
    print(result)

