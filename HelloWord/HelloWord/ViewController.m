//
//  ViewController.m
//  HelloWord
//
//  Created by grx on 2020/6/10.
//  Copyright © 2020 ruixiao. All rights reserved.
//

#import "ViewController.h"
/*
 *  字符串混淆解密函数，将char[] 形式字符数组和 aa异或运算揭秘
 *  如果没有经过混淆，请关闭宏开关
 */
extern char* decryptConstString(char* string)
{
    char* origin_string = string;
    while(*string) {
        *string ^= 0xAA;
        string++;
    }
    return origin_string;
}


//字符串混淆加密 和 解密的宏开关
#define ggh_confusion
#ifdef ggh_confusion
    #define confusion_NSSTRING(string) [NSString stringWithUTF8String:decryptConstString(string)]
    #define confusion_CSTRING(string) decryptConstString(string)
#else
    #define confusion_NSSTRING(string) @string
    #define confusion_CSTRING(string) string
#endif

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // 暂不支持中文
    NSString *hello = confusion_NSSTRING(((char []) {226, 207, 198, 198, 197, 138, 221, 197, 216, 198, 206, 0}));
    NSLog(@"混淆结果====%@",hello);
}


@end
