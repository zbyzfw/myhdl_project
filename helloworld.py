from myhdl import block, Signal, delay, always, now

@block
def HelloWorld():

    clk = Signal(0)  # 定义一个时钟信号

    @always(delay(10))  # always总是运行,delay当超过指定的延迟间隔时，将执行该函数
    def drive_clk():
        # 驱动时钟信号函数 它定义了在一定延迟后连续切换时钟信号的生成器。信号的新值是通过赋值给它的next属性来指定的。这是与VHDL信号assign和Verilog非阻塞分配等效的MyHDL。
        clk.next = not clk

    @always(clk.posedge)  # 将在每个上升的时钟边缘上执行。
    def say_hello():
        print("%s Hello World!" % now())

    return drive_clk, say_hello


inst = HelloWorld()
inst.run_sim(50)
