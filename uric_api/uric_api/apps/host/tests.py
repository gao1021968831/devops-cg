from django.test import TestCase

# Create your tests here.
# import paramiko
# import traceback
# from paramiko.ssh_exception import AuthenticationException
# from paramiko.rsakey import RSAKey
# from io import StringIO
#
# if __name__ == '__main__':
#     # 通过parammiko创建一个ssh短连接客户端实例对象
#     ssh = paramiko.SSHClient()
#     # 自动在本机第一次连接远程服务器时，记录主机指纹
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     try:
#         # 1. 直接密码远程连接的方式
#         # ssh.connect(hostname='47.112.179.213', port=22, username='root', password='Bazinga$yuan', timeout=10)
#         # 注意，如果你测试某个服务器的连接时，如果你本地已经配置了这个远程服务器的免密登录(公私钥模式)，那么就不能测试出密码是否正确了，因为首先会通过公私钥模式登录，不会使用你的密码的。
#         # 2. 使用秘钥免密登录的方式
#         # pkey = PkeyModel.objects.get(name='').private
#         private_key = '''-----BEGIN RSA PRIVATE KEY-----
# MIIEpQIBAAKCAQEAu4zbB24ZrFoQCKvyytczzHLIqobpWQtWKHzxxA0PG3d0HCRJ
# boTyYIH8GYYhAwVXXnolezpFI2rrrVan0E6+EVPXq50mdAGmk9iIYFiYpm6tpjRF
# Jf0qNRQRM1mj9Jt1Ae9TreQwEmPVsnMBgVJRAhrWG4BsnmK2gN4mfzqLRhntw7ZJ
# URTjyP5+L03gVt0N3Cq6+9E5k/lBtbf2JZYTRacprCghZ5Ml5tDLU7K2nHwTODnd
# Iawo7cVCInWzHWGR2KvhWPtvbJXC0+6M6tkic+DOSSlc2gJtpQPsHpTvwcVpcIvp
# irtTZUoFSHt/aeXdLH0c28OGSNt4Nuynyd4SjQIDAQABAoIBACZaw24tD3YGQxIq
# 6++ce/zbGnt5NJ5fqaKFDsI7s3O4BZg9uYCvEow2+PHVUsn13Sy2iRS+0WXRV1ov
# BwmcGNWdUlVHwZXmwoSouxcM90bOCpgbR2rh77BEJtJcCiIbap3XLkM5D7WrEgg4
# 6b1jMqreBxw/srbfVBhdlfzd4Z6XlDqmSMuVEdHFESwie1XfxA76d+isdD3XWpzQ
# YTaXYIrjR8qDFDARDa/6LR47Rotz7t4HJo8FaB84S2mBrzwuP5+2eQVV2VJK98fG
# NRbho3xS5GJEgazXCaLly9GosVaGPNXWpGPwXzTqyqlvd3g7m1+imEttAV0MCqBO
# uawIUicCgYEA36sfSnewRVlA7aYaH2PiYODCk3Oy8IF74rfBdfxoWKJK/G274jAw
# qi13Qn2QPP/O1oGkqv8XBk/ic7Mr7hL5by2STbmaL54AWe8XOI2PEbQjFHSgEu43
# 93SkeRDlJEJHKFZGZ6fI8rEn0zaQo12R4ChX15ow/Ka/9hDo1bJE7NMCgYEA1qks
# hy88MZVcpc0LsKsZvC6FN/cgOc4RhMU7uzshuyr63RwjoYkYA3bOBQXXWv0n5ala
# 5fAx7B6SBq5gazO7XxNjmQgkLj2wKL+YNpMoujGkZ1cB1fF4JZCzNlx1abxC5C9N
# UyeSRMqsNS3ZnP4CrurgLKAHvq9dhJFRMHcB5x8CgYEApXqueOLaaERjlC+q7gRx
# TSmc64jTH7s80/0NxeQLs1/HSMFLG0p6Br4CmQ/a8jZ0aiGameSGvWXG7cDmxIoH
# P2kg8B5cY9RrAB6zOGULL5btyUmL0NWsVIlY0jVcwpnCmaZTCoeJVX0aMNsS4brt
# nUFb1CjBC3u3VC8ohEoTUn8CgYEAv5eTVL1GHoNPg/S1YGP2vk1PPhpmOvHAFR7t
# Jzmp66J68erxqnXwZvcc/sKt6lpVx9gWd3ChPjwy3Z+6EzTDIiLuHGJ12IfauSP4
# uY0zJqy0LkAsNUYmlHDIY9a2PT94/K1zeKqzFI9IkNZxinv07SZaG7ph70IaV/5T
# 1swBeMUCgYEAxEdz0VPx7+B7lfgn2LmDyevIAaJMMRpazy6PjpXKRAKjFpH6pEGB
# 6upHz7+fdN6sRCrSmqLZPbKLqP4cWf5WCeeWK9WRlpgnDRnNKrKee279QT5nREol
# mUBjo0eLCCF3qcQilCiZBNDTzGXdJNH0Krf4oeKbfco199OCR3g82WA=
# -----END RSA PRIVATE KEY-----'''
#         pkey = RSAKey.from_private_key(StringIO(private_key))
#         ssh.connect(hostname='1.13.248.79', port=2222, username='deployer', pkey=pkey, timeout=10)
#
#         # 连接成功以后，就可以发送操作指令
#         # stdin 输入[本机发送给远程主机的信息]
#         # stdout 输出[远程主机返回给本机的信息]
#         # stderr 错误
#         stdin, stdout, stderr = ssh.exec_command('ls -la')
#         # 读取stdout对象中返回的内容，返回结果bytes类型数据
#         result = stdout.read()
#         print(result.decode())
#         # 关闭连接
#         ssh.close()
#     except AuthenticationException as e:
#         print(e.message)
#         print(traceback.format_exc())
#         print("连接参数有误，请检查连接信息是否正确！~")