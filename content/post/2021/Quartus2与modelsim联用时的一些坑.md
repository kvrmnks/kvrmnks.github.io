---
title: Quartus2与modelsim联用时的一些坑
date: 2021-05-02 09:56:07
tags: ["计算机组成原理"]
---
调试的时候姑且做了一个调试笔记, 稍微列一些回忆中的坑吧.
<!-- more -->

---

安装ModelSim的时候一定要保证和Quartus版本号一致

---

### 由Verilog中产生的 "bug"

Verilog中的initial模块在下载到开发板上时并不会生效.

所谓的"初始化"仅仅在模拟中生效.

所以严格来说还是要加一个信号来对寄存器进行初始化.



Verilog 在Quartus中编译时一定要看其中的警告信息, 因为verilog允许了隐式声明一个wire

例如我有一个module abab(input[3:0] a);

在调用时直接写了 abab xxx(b); 隐式产生了一个wire b, 但是这个隐式产生的信号b只有一个bit长, 并不是4bit长的.

同样的使用assign 隐式来定义一个wire 也会产生如上的 "bug".



Verilog 中对于输入的长度没有做到严格的匹配, 比如上文中的

module abab(input[3:0] a);

我也可以, 这样传参

wire [100:0] b;

abab xxx(b);

这样虽然可以过编译, 但是在RTL模拟中会出现一些奇怪的bug  比如输出为"z".



还有是Verilog中同时检测两个信号的always, 不过这里我也不知道正统的方法是什么, 为了保证正确.

最好采取如下写法

```
always @(posedge clk or negedge rst) begin
	if(!rst) begin
		...
	end else begin
		..
	end
end
```

---

### 由Quartus产生的"bug"

Quartus中的仿真功能不能看到仿真后的内存情况.

可以通过采取使用Quartus生成测试文件, 通过modelsim进行模拟仿真的方式.

这个方式需要自己写testbench文件.

仿真的步骤可以查看这个[视频](https://www.bilibili.com/video/BV1Ez411z7xf)

期间可能遭遇无法正确加载RAM&ROM 初始化文件的情况, 可以查看这个[链接](https://blog.csdn.net/weixin_44939178/article/details/111928005)



Quartus编译过程中包含了许多在仿真过程中可能用不到的工序.

对于RTL模拟(功能模拟)来说, 并不需要在Quartus中重新编译, 只需要关掉ModelSim 重新进行仿真就可以了.

而对于时序模拟来说, 需要重新编译.

利用这些步骤可以加快debug速度, 当然最稳健的方式还是每次重新编译.



Quartus中重新编译并不会自动产生testbench文件, 需要手动按按钮来生成.



---

### 由ModelSim 产生的"bug"



你可能会发现仿真结果在时序仿真和功能仿真下结果不一样.

这种情况十分有风险, 尽可能保证两种仿真下结果一致.

但是时序仿真中无法查看ROM&RAM中的数据.

在功能仿真中可以, 具体方式可查看这个[链接](https://www.cnblogs.com/halflife/archive/2011/03/08/1977508.html)



同时在时序仿真的时候一定要注意时钟间隔不能太短，否则可能会导致计算结果还没稳定的时候就进行了下一步。

---

无了, 祝好.


