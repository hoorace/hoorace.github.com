---
comments: true
date: 2015-06-11 12:30:00
layout: post
slug: mac-osx-clean-by-hand
title: 手动清理MAC 文件的方法
categories:
- review
tag:
- mac
- cache
- itunes

---


    <p>&nbsp;&nbsp;&nbsp;&nbsp; 由于mac平时不怎么重启，还有就是买了iphone6 64G后发现mac的硬盘根本就不够用了，手机和pad的自动备份到硬盘的确耗费了很多资源，使用appcleaner删除一些大的应用后还是不能满足需求，所以只能手动删除不需要的内容。</p>

    #### <p>1：清理iTunes中的手机备份文件</p>

    <p>&nbsp;&nbsp;&nbsp;&nbsp;iphone或者是ipad连接到电脑，打开iTunes，打开“文件 > 系统偏好设置” 找到设备，删除其中的备份文件。</p>

    #### <p>2：清理icloud的备份文件</p>
    <p>2.1 查找文件</p>
    cd ~/Library
    du -sh * | sort -n

    <p>2.2 找到大的文件记录，删除移动端备份文件 (如果手动备份了iCloud)</p>
    cd Application\ Support/MobileSync
    rm -rf Backup

    #### <p>3: 清理缓存文件和日志</p>
    <p>3.1 清理缓存文件：</p>
    cd ~/Library/Caches/
    rm -rf *
    <p>3.2 清理缓存文件(系统重启的时候会自动清理，当时MAC很少关机重启)：</p>
    sudo rm -rf /private/var/log/*

    <p>3.3 清理临时文件</p>
    cd /private/var/tmp/
    rm -rf *

    <p>3.4 清理Xcode的模拟器文件</p>
    ``` shell
    cd /Users/longhao/Library/Developer/Xcode/iOS\ DeviceSupport
    ```
    选择需要删除的模拟器信息
