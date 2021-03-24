# coding=utf-8
import os


class ConfigChange:
    def __init__(self, path):
        # cur_path = os.path.dirname(os.path.realpath(__file__))
        self.yml_path = os.path.join('/apps/apache-tomcat-icdm/webapps/icdm-controller/WEB-INF/classes/', path)

    def change_yml_str(self):
        '''
        通过匹配字符串修改相关配置
        :return:
        '''
        print('*' * 40)
        print('-->开始修改【{}】配置文件'.format(self.yml_path))
        with open(self.yml_path, mode='r', encoding='utf-8') as y:
            data = y.read()
            print('当前配置文件内容为：\n{}'.format(data))
            # 修改第一个spring配置
            data = data.replace('showSql: true', 'showSql: false')
            # 修改第四个spring配置
            data = data.replace('jdbc:oracle:thin:@192.168.8.76:1521:orcl',
                                'jdbc:oracle:thin:@192.168.1.53:1521:orcl')  # 修改数据库连接
            data = data.replace('yfrh', 'icdm')  # 修改用户名密码
            # 修改第八个spring配置（开放平台消息队列配置）
            data = data.replace("39.98.107.44", "192.168.1.46", 1)  # rabbitmq服务ip,第三个参数1表示修改最大次数不超过1次
            # 修改system配置
            data = data.replace("http://192.168.8.99:8023/pm-oauth/pos/sessions",
                                "http://192.168.1.46:8080/pm-oauth/pos/sessions")  # 修改开放平台接口路径
            data = data.replace("D:/file/", "/apps/apache-tomcat-icdm/upload/")  # 修改文件上传路径前缀
            data = data.replace("D:/file/exportTemp", "/apps/apache-tomcat-icdm/upload/exportTemp")  # 导出文件临时目录路径前缀
            # thirdParty
            data = data.replace('192.168.8.99:8082', '192.168.8.230:8080/ph-s-repor')  # 修改公卫接口路径
        print('修改后的配置文件内容为：\n{}'.format(data))
        print('-->配置文件修改完毕')
        print('*' * 40)
        print('-->开始写入【{}】配置文件'.format(self.yml_path))
        with open(self.yml_path, mode='w', encoding='utf-8') as w:
            w.write(data)
        print('-->配置文件写入完毕')


ConfigChange('application.yml').change_yml_str()
