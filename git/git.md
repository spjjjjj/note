配置用户名邮箱地址
git config --global user.name 'XXXX'
git config --global user.email XXXXXXXXX@qq.com

初始化本地项目（用于git提交到github仓库）
git init

将所有更改添加到暂存区
git add .

git commit 命令用于将暂存区的更改记录到本地 Git 仓库中，形成一个新的提交快照。
命令格式:
git commit -m "提交信息"
其中，-m 选项后跟的字符串是本次提交的说明信息，用于描述这次提交的目的和内容。
提交的功能

将本地 Git 仓库与远程仓库关联起来
git remot add origin git@github.com:spjjjjj/note.git

拉取仓库中的代码，最好每次都拉取。
git pull origin master
todo：检查冲突

将本地的master分支的更改推送到远程仓库
git push -u origin master
-u参数是--set-upstream的简写，这个参数在推送时会将本地分支与远程分支关联起来。
这样做的好处是，下次你在同一个分支上使用git push时，就不需要再指定远程仓库和分支名了。
Git会记住你上一次推送的远程仓库和分支，自动将本地分支的更新推送到之前指定的远程分支。
使用这个命令后，如果你在master分支上有新的更改，下次只需简单地输入git push，Git就会将更改推送到origin的master分支。

查看更新日志
git log --pretty=oneline
--pretty=oneline 每次更新内容在一行内展示
--graph 以 ASCII 图形显示分支和合并历史。q退出   f向下翻页 b向上翻页 j下滚 k上滚
最新的在上面,hash
todo:format 占位符

git checkout <hash>






todo:多个仓库管理
todo：更改某一版本的内容
todo：分支相关