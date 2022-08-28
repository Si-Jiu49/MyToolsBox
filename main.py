from os import walk
import easygui as eg

toolsPath = "./Tools"
boxVersion = '22y35w_dev'
repo_site = "https://github.com/Si-Jiu49/MyToolsBox"


def scanning_tools():
    # TODO 扫描Tools目录下的所有工具
    for root, ds, fs in walk(toolsPath):
        yield from fs


def menu():
    choose = eg.choicebox("请选择工具：", title="选择工具", choices=[n.strip(".py") for n in scanning_tools()])
    if choose is None:
        eg.msgbox("您还未选择任何工具，请重试")
        menu()
    secondary_menu(choose)


def secondary_menu(name):
    if eg.ynbox(f"是否要执行程序：{name}？", "执行？", ["Yes", "No"], cancel_choice="[<N>No]"):
        exec(open(f"./Tools/{name}.py", 'r', encoding="utf-8").read())
        menu()


def main():
    if eg.ynbox(
            f"""欢迎使用MyToolsBox工具箱
 这是一个小学生自编的工具箱，里面含盖了大家日常生活中常用的功能，写作业时偷懒或者其它的功能
当前版本为{boxVersion}
repo地址：{repo_site}
请问是否继续？""", "前言", ["继续", "退出"]):
        menu()
    else:
        exit(114514)


if __name__ == '__main__':
    main()
