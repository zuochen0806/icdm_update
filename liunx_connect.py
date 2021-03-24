import paramiko


class LinuxConnect:
    def __init__(self, ip, port, username, password):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def remot_connect(self):
        '''
        配置服务器相关信息
        :return:
        '''
        # 创建SSHClient 实例对象
        self.ssh = paramiko.SSHClient()
        # 调用方法，表示没有存储远程机器的公钥，允许访问
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接远程机器，地址，端口，用户名密码
        self.ssh.connect(self.ip, self.port, self.username, self.password, timeout=10)
        print('-->服务器[{}]连接成功'.format(self.ip))

    def run_cmd(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        # 输出命令执行结果
        result = stdout.read()
        print(result)
        # return result

    def linux_business(self):
        '''
        执行组合操作
        :return:
        '''
        print('-->开始执行组合操作')
        self.remot_connect()
        print('-->删除项目，初始化环境')
        self.run_cmd('rm -rf /apps/apache-tomcat-icdm/webapps/icdm-controller')
        print('-->解压项目')
        self.run_cmd('unzip /apps/icdm/icdm-controller.war -d /apps/apache-tomcat-icdm/webapps/icdm-controller')
        print('-->修改配置文件')
        self.run_cmd('python /apps/apache-tomcat-icdm/configchange/icdm_server_config_change.py')
        print('-->重启tomcat')
        self.run_cmd('kill -9 `ps -ef | grep apache-tomcat-icdm | grep -v "grep" | awk "{print $2}"`')
        self.run_cmd('/bin/bash /apps/apache-tomcat-icdm/bin/startup.sh ')
        print('-->已重启，请等待...')

    def close(self):
        self.ssh.close()
        print('-->关闭连接')


# lc = LinuxConnect('192.168.1.62', '22', 'root', 'yunwei2020')
lc = LinuxConnect('192.168.8.230', '22', 'root', 'Gxrj2020')
lc.linux_business()
lc.close()
