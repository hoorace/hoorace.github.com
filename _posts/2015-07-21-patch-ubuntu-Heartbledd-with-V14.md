---
comments: true
date: 2015-07-21 11:42:30
layout: post
slug: patch-ubuntu-Heartbledd-with-V14
title: HeartBleed Ubuntu 修复问题记录
categories:
- linux
tag:
- ubuntu
- heartbleed
- openssl

---
<p>&nbsp;&nbsp;&nbsp;&nbsp;在安装某linux软件的时候，提示我们的服务器上的openssl是有漏洞的版本，需要重新安装一下。到linuxe服务器上查看一下：
```sh
dpkg -l | grep "openssl”
openssl                                  1.0.1f-1ubuntu2.8                amd64
```
</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;1.0.1f 是HeartBleed的版本之一，需要修复问题。</p>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 1：卸载旧版本的openssl</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">

```sh
apt-get purge openssl
rm -rf /etc/ssl
```

</div>

<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 2：安装新版本的openssl</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p>&nbsp;&nbsp;&nbsp;&nbsp; 安装版本</p>
<div>

```sh
wget https://www.openssl.org/source/openssl-1.0.2d.tar.gz 
tar zxvf openssl-1.0.2d.tar.gz
./config  --prefix=/usr/local --openssldir=/usr/local/ssl
make && make install
./config shared --prefix=/usr/local --openssldir=/usr/local/ssl
make clean
make && make install
```

</div>
<p>&nbsp;&nbsp;&nbsp;&nbsp;链接openssl <br />
```js
ln -sf /usr/local/bin/openssl `which openssl`

```
</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;链接openssl <br />

```sh
openssl version
```
</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;安装openssl之后，有些以前编译的软件会出现无法使用的情况，报错为：/usr/local/lib/libssl.so.1.0.0: no version information available
需要重新编译一下。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;</p>
</div>

<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 3：OR 打patch的方式来处理</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p>&nbsp;&nbsp;&nbsp;&nbsp;patch地址：<a href="https://launchpad.net/ubuntu/+source/openssl/1.0.1-4ubuntu5.12" target="_blank">https://launchpad.net/ubuntu/+source/openssl/1.0.1-4ubuntu5.12</a> </p>
```sh
wget http://www.openssl.org/source/openssl-1.0.1f.tar.gz
tar -xvf openssl-1.0.1f.tar.gz
wget https://launchpad.net/ubuntu/+archive/primary/+files/openssl_1.0.1f-1ubuntu1.debian.tar.gz
tar -xvf openssl_1.0.1f-1ubuntu1.debian.tar.gz
mv debian openssl_1.0.1f-1ubuntu1 (just because that's what I did)
cd openssl-1.0.1f/
patch -p1 < ../openssl_1.0.1f-1ubuntu1/patches/version-script.patch
./config
make
make test
sudo make install
```

</div>
<p>&nbsp;&nbsp;&nbsp;&nbsp; </p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;参考文档： </p>
- [x] <a href="http://askubuntu.com/questions/444702/how-to-patch-the-heartbleed-bug-cve-2014-0160-in-openssl" target="_blank">How to patch the Heartbleed bug (CVE-2014-0160) in OpenSSL?</a>
- [x] <a href="http://wangyan.org/blog/install-openssl-from-source.html" target="_blank">Linux 从源码编译安装 OpenSSL</a>
- [x] <a href="http://heartbleed.com" target="_blank">http://heartbleed.com</a>