# VOom-enhance
Enhancements for vim plugin VOom.
## 1. 自动生成小说目录
### 用法：
1. 在 Vim 中安装 VOom 插件。[VOom 链接](https://github.com/vim-scripts/VOoM)

2. 将 voom_mode_chapter.py 放入 'VOom/autoload/voom' 目录.

3. 现在可以用 ':Voom chapter' 命令来生成目录了。或者你也可以在 vimrc 中添加如下内容：

```
function! Def_Voom()
  if &filetype == '' || &filetype =='text'
    :VoomToggle chapter	
  "elseif &filetype =="markdown"
	"	:VoomToggle markdown
	"elseif &filetype == "pandoc"
	"	:VoomToggle pandoc
	"elseif &filetype =="org"
	"	:VoomToggle org
	else
		:VoomToggle
	endif
endfunction
noremap <silent> <F11> :call Def_Voom()<CR>
inoremap <silent> <F11> <esc>:call Def_Voom()<CR>
```
这样你就可以用 F11 键快速生成目录了。

（注意：对于十几兆大小的长篇小说，这个脚本在执行的时候会有几秒钟的卡顿。不过，并不会卡太久。）
### 样式
1. 支持以'#'开头的 Markdown 式标题。

2. 支持以诸如「第一章」、「第一卷」等开头的小说标题。（目前只能生成第一级标题。）
3. 想要其他效果请自行添加。
### 截图

![截图1](https://github.com/Ex-mortal/VOom-enhance/blob/master/images/1.png)
![截图2](https://github.com/Ex-mortal/VOom-enhance/blob/master/images/2.png)
