# 综述
  - 程序提供判断输入的字段是否为预期的类型服务，遵循RESTful架构，采用flask框架实现，使用gunicorn管理进程服务。<br/>
  - 程序使用swagger说明API文档，swagger服务随接口服务一起启动。

# 安装依赖
  - 进入bin目录，运行脚本文件requirement_install.sh，即可安装依赖。

# 环境
  - Python2.7
  - Linux 64

# 数据文件
  - 由于数据文件较大，stash上有限制项目大小。所以数据文件单独存放在"\\192.168.1.180\中转站\freychen\resume_check_data.tar".下载后，解压覆盖data/目录即可。

# 启动服务
  - 使用python运行resume_check_api文件夹下的main.py

# 请求路径信息
  - port: 9003
  - 路径: /value_check　# 检测单个value接口
  - 路径: /batch_check　# 检测多个value接口
  - 路径: /company/clean　# 检测单个value是否为company，如果是那么对其进行清洗
  - 路径: /company/batch_clean # 检测多个value是否为company，如果是那么对其进行清洗
  - 路径: /position/clean　# 检测单个value是否为position，如果是那么对其进行清洗
  - 路径: /position/batch_clean # 检测多个value是否为position，如果是那么对其进行清洗
  - 方法: post
  - swagger路径为： /doc/

# 输入要求
  - 现在仅支持company和position的检测,所以label的值有0和1两个，其具体含义如下：
	- 0:'comp'
	- 1:'posi'

  - 其他要求见swagger页面。

# 测试
  - 测试分为程序性能测试和效果测试两个部分。性能测试含有两个功能用来测试程序执行一次批量处理所需要的时间，**不能测程序并发性能**，。
  - **性能测试**，性能测试含有两个功能：时耗测试与时耗分析。
    + 时耗测试，用来测试程序执行一次批量处理所需要的时间，**不能测程序并发性能**。测试文件为“test_by_requests.py”。测试的是服务的性能，所以应该先将服务开启，服务的配置部分源码如下：
      ```python
      def test_time(data):
          res = requests.post("http://0.0.0.0:8001/position/batch_clean", data=json.dumps(data))
          cost_time = json.loads(res.text)['cost_time']
          cost_times.append(cost_time)
          return cost_time
      ```
      代码会输出129次测试的平均时耗，因为时耗会受机器性能影响，所以最好测试优化前和优化后的两个版本时间消耗，然后计算其比值。请将测试后的结果追加到[时耗文件](http://192.168.1.61:8090/pages/viewpage.action?pageId=21299508)中。

    + 时耗分析，分析处理一次请求时各个函数的时间消耗，文件是“time_analyse.py”.

  - **效果测试**，可以作为回归测试，文件是"test_position.py"。如果文件输出一致，则回归测试成功，否则为失败，进一步分析原因。不一定是改进后程序出问题了，有可能是，标准答案有问题。

# 各个环境接口地址
  这里只有IP和端口号，如果需要具体路径，请访问swagger页面确定。如果服务挂了可以找Balance重启。
  - rc环境：http://192.168.1.31:8001/
  - stg或线上内网环境 http://resume-check-internal.hireye.com/position/batch_clean
  如果性能达不到，应该是机器资源不够或者别的问题，请找Balance确定。


# helper文件夹
  - 文件夹的ipynb文件，提供数据录入、预处理和训练模型功能，为程序提供数据和模型支撑。详情见helper/readme.md.