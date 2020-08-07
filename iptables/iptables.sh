#!/bin/bash

# 开启iptables的DROP模式
drop(){
    echo "即将开启iptables策略,请稍后"
    systemctl start iptables
    iptables -P INPUT ACCEPT && iptables -F && iptables -X && iptables -Z && iptables -A INPUT -p tcp --dport 22 -j ACCEPT && iptables -P INPUT DROP
    service iptables save
}

# 清空所有iptables策略
Clear(){
    iptables -P INPUT ACCEPT && iptables -F && iptables -X && iptables -Z
    iptables -A INPUT -p tcp --dport 22 -j ACCEPT && iptables -P INPUT DROP
}

# 允许本机某个端口接受流量的访问
accept(){
    read -p "请输入接受访问的端口:" n
    iptables -A INPUT -p tcp --dport $n -j ACCEPT
}

# 不允许本机访问的外部网络
noacc(){
    read -p "请输入不允许访问网络的ip:" n
    iptables -A OUTPUT -d $n -j DROP
}

# 不允许外部网络访问主机的某个端口
noinacc(){
    read -p "请输入外部网络ip:" ip
    read -p "请输入本机端口:" n
    iptables -I INPUT 1 -s $ip -p tcp --dport $n -j DROP
}

# 删除iptables策略
del(){
    iptables -L --line-number
    read -p "请输入你要删除策略的序号:" n
    count=$(iptables -L --line-number | grep ssh | grep -v grep | awk '{print $1}')
    for i in $count
    do
        if [ $i -eq $n ];then
            echo "ssh端口不允许删除"
        else
    	    iptables -D INPUT $n
        fi
    done
}

# 是否需要保存修改策略
judge(){
    read -p "不保存修改策略,请输入n:" key
    if [ "$key" == n ];then
        main
    fi
    service iptables save
}
main(){
    echo "退出程序，请输入0"
    echo "清空所有iptables策略，请输入1"
    echo "开启某个端口的允许外部访问，请输入2"
    echo "不允许本机网络访问某个外部网络，请输入3"
    echo "不允许某个网络ip访问本机的某个端口，请输入4"
    echo "删除iptables策略，请输入5"
    read -p "请输入:" n
    case $n in
    0)
        exit 0;;
    1)
        Clear
        judge
        main;;
    2) 
        accept
        judge
        main;;
    3) 
        noacc
        judge
        main;;
    4) 
        noinacc
        judge
        main;;
    5) 
        del
        judge
        main;; 
    *)
        echo "你输入序号不在功能选项里,请重新输入"
        main;;
    esac
}

num=$(systemctl status iptables | grep 'Active: active (exited)' | wc -l)
if [ $num -eq 0 ];then
    drop
fi
main
