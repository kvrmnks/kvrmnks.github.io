---
title: cmake的坑
date: 2021-06-13 11:32:55
tags: ["CMake"]
---
## cmake的坑。。。

#### cmake并不在mingw中

嗯，需要重新安装。。

#### vscode terminal的环境变量需要重启vscode才能生效

#### mingw 中的“make” 叫做“mingw32-make”

#### cmake 默认使用vs的那套工具栈

也就是说需要

cmake -G "MinGW Makefiles" [directoty]

注意这里大小写敏感!

#### 参数没有逗号分隔

---

### 常用指令&功能

#### 设置变量

```cmake
# set(Key Value)
set(ABAB 1)

# 需要使用${ABAB}来获取这个变量的值
```

#### 常用变量

PROJECT_SOURCE_DIR 当前工程的最上层目录

PROJECT_BINARY_DIR 当前工程的构建目录，一般指执行cmake的pwd

#### 添加头文件

```cmake
include_directories()
```



#### 复制替换文件

```cmake
configure_file(<input>, <output>)
```

此命令可以将input复制到output同时替换文件中@VARIABLE@的值，替换成为变量



#### 递归CMakeLists.txt

```cmake
#添加
add_subdirectory()
```



#### 生成链接文件

```cmake
add_library() #用法基本与add_executable()相同
```

#### link链接文件

```cmake
target_link_libraries() #用法基本与add_executable()相同
```



#### 生成选项

```cmake
if()
endif()
```

```cmake
option(FLAG "help text" <ON/OFF>)
# 使用时可以进行命令行传参
```
