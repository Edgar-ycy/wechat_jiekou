from toolkit.wechat import XiaomiSport

from flask import Flask, render_template, redirect, url_for
from flask import request
import time


def change(user: str, passwd: str, number: int):
    """

    :param user: 账号
    :param passwd: 密码
    :param number: 步数
    :return: 字符串结果
    """
    print(f'手机号:{user},\t密码: {passwd}, \t步数:  {number}, 正在修改')
    # try:
    #     # 执行一键修改步数
    #     XiaomiSport(user, passwd, number).one_click_change_step()
    #     return user, passwd, number, '完成'
    # except Exception as e:
    #     print('运行出错，原因：%s' % e)
    #     return f'运行出错，原因：{e}'

        # 最大运行出错次数
    try:
        # 执行一键修改步数
        work = XiaomiSport(user, passwd, number).one_click_change_step()
        return work
    except Exception as e:
        print('运行出错，原因：%s' % e)
        return f'运行出错，原因：{e}'




app = Flask(__name__)  # 获取实例


@app.route('/')
def start():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return redirect(url_for('steps'))


@app.route('/steps', methods=['POST', 'GET'])
def steps():
    error = None
    if request.method == 'POST':
        if request.form['name'] and request.form['passwd'] and request.form['number']:
            datas = request.form['name'], request.form['passwd'], int(request.form['number'])
            # error = f"账号为: {datas[0]} \n密码为: {datas[1]} \n步数为: {datas[2]}"
            error = change(*datas)
        else:
            error = 'Invalid username/password'

    return render_template('change_step.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15520, debug=True)
