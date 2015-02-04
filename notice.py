# -*- coding:utf-8 -*-
import urllib

def csNotice():
    # 抓取站点
    cssite="http://cs.njust.edu.cn"
    csurl="http://cs.njust.edu.cn/s/56/t/414/p/5/list.htm"
    content=urllib.urlopen(csurl).read()
    
    # 内容分解
    info1="' target='_blank' style=''><font color=''>"
    info2="</font></a></td></tr></table></td>"
    info3="<td><table width=100% border=0 cellspacing=0 cellpadding=0 class='columnStyle'><tr><td><a href='"
    deploy_time="发布时间:"
    read_num="</span><span>浏览次数:"
    
    # 遍历保存
    title_link_time=[]
    content1=content
    content2=content
    while content1.count(info1):
        # title
        index1=content1.find(info1)
        content1=content1[index1+42:]
        index2=content1.find(info2)
        a=content1[0:index2]
        # link
        index1=content2.find(info3)
        content2=content2[index1+96:]
        index2=content2.find(info1)
        b=content2[0:index2]
        # time
        content3=urllib.urlopen(cssite+b).read()
        index1=content3.find(deploy_time)
        index2=content3.find(read_num)
        c=content3[index1+13:index2]
        dict={}
        dict['school']="计算机院"
        dict['title']=a
        dict['link']=cssite+b
        dict['time']=c
        title_link_time.append(dict)
    return title_link_time

def damsNotice():
    # 抓取站点
    dasite="http://dams.njust.edu.cn"
    csurl="http://dams.njust.edu.cn/index.html"
    content=urllib.urlopen(csurl).read()
    
    # 内容分解
    info1="""<li><img src="/templets/default/images/a2.jpg" />"""
    info2="""">"""
    info3="</a><em>["
    info4="时间:"
    
    # 遍历保存
    title_link_time=[]
    while content.count(info1):
        index1=content.find(info1)
        content1=content[index1+58:]
        index2=content1.find(info2)
        link=dasite+content1[0:index2]
        content2=content1[index2+2:]
        index3=content2.find(info3);
        title=content2[0:index3]
        content=content2[index3:]
        # get link
        content3=urllib.urlopen(link).read()
        index4=content3.find(info4)
        content3=content3[index4+7:]
        time=content3[0:10]
        dict={}
        dict['school']="设传学院"
        dict['title']=title
        dict['link']=link
        dict['time']=time
        title_link_time.append(dict)
    return title_link_time

def semNotice():
    # 抓取站点
    csurl="http://sem.njust.edu.cn/?cat=41"
    content=urllib.urlopen(csurl).read()
    
    # 内容分解
    info1="post type-post status-publish format-standard hentry category-41 no_owl_sticky"
    info2="""">"""
    info3="</a>"
    info4="</span></li>"
    # 遍历保存
    title_link_time=[]
    while content.count(info1):
        index1=content.find(info1)
        content1=content[index1+86:]
        index2=content1.find(info2)
        link=content1[0:index2]
        content2=content1[index2+2:]
        index3=content2.find(info3)
        title=content2[0:index3]
        index4=content2.find(info4)
        time=content2[index3+31:index4]
        content=content2[index4:]
        dict={}
        dict['school']="经管学院"
        dict['title']=title
        dict['link']=link
        dict['time']=time
        title_link_time.append(dict)
    return title_link_time

def gsNotice():
    
    gsurl="http://gs.njust.edu.cn"
    content=urllib.urlopen(gsurl).read()
    # gb2312-unicode-utf-8
    a_unicode = content.decode('gb2312')
    content = a_unicode.encode('utf-8')
  
    # 内容分解content
    info1="<li><p>・</p><em>"
    info5="""" target"""
    info2=""">"""
    info3="</a><span>"
    info4="</small>"
    # 遍历保存
    title_link_time=[]
    i=0
    while content.count(info1) & i<14:
        index1=content.find(info1)
        content1=content[index1:]
        index2=content1.find(info5)
        link=gsurl+content1[43:index2]
        
        content2=content1[index2:]
        index3=content2.find(info2)
        index4=content2.find(info3)
        title=content2[index3+1:index4]
        content=content2[index4:]
        
        # 抓取时间
        content3=urllib.urlopen(link).read()
        index5=content3.find(info4)
        time=content3[index5+8:index5+19]
        dict={}
        dict['school']="研究生院"
        dict['title']=title
        dict['link']=link
        dict['time']=time
        title_link_time.append(dict)
        i=i+1
    # sort
    def timeSort(s):
        return s['time']
    title_link_time=sorted(title_link_time,key=timeSort,reverse=True)
    return title_link_time

def lxyNotice():
    
    gsurl="http://lxy.njust.edu.cn"
    content=urllib.urlopen(gsurl).read()
    
    # 内容分解content
    info1="<td><table width=100%  cellpadding=0 cellspacing=0 border=0><tr><td align=left><a href='"
    info2="""' target=_blank title="""
    info3="""">"""
    info4="</a></td><td  width='50' align=right><div style='white-space:nowrap'>"
    # 遍历保存
    title_link_time=[]
    i=0
    while content.count(info1) & i<5:
        index1=content.find(info1)
        content1=content[index1+88:]
        index2=content1.find(info2)
        link=gsurl+content1[0:index2]
        index3=content1.find(info3)
        index4=content1.find(info4)
        title =content1[index3+2:index4]
        content2=content1[index4:]
        time=content2[69:79]
        content=content2[79:]

        dict={}
        dict['school']="理学院"
        dict['title']=title
        dict['link']=link
        dict['time']=time
        title_link_time.append(dict)
        i=i+1
    return title_link_time 

cs=csNotice()
cs=cs[0:min(5,len(cs))]
dams=damsNotice()
dams=dams[0:min(5,len(dams))]
sem=semNotice()
sem=sem[0:min(5,len(sem))]
gs=gsNotice()
gs=gs[0:min(5,len(gs))]
lxy=lxyNotice()
lxy=lxy[0:min(5,len(lxy))]
merge=cs+dams+sem+gs+lxy

# 排序
def timeSort(s):
    return s['time']
merge=sorted(merge,key=timeSort,reverse=True)

print "Content-type: text/html"
print ""
print "<html><head>"
print """<meta charset="UTF-8">"""
print """<link rel="stylesheet" href="style.css"">"""
print """<link rel="shortcut icon" type="image/x-icon" href="favicon.ico" media="screen" />"""

print "<title>校园通知公告汇总</title>"
print """</head><body>"""

print "<hr>"
print """<h1><center>校园Notice&nbsp;<img src="favicon.ico"/></h1>"""
print """<div class="panel-body">"""
print """<div class="table-responsive">"""
print """<table class="table table-striped table-bordered preach-table" style="font-size:13px">
	<tr>
		<td><b>院系</td>
		<td><b>时间</td>
		<td><b>标题</td>
	</tr>"""
	
# 选取前五行
for elem in merge:
	print "<tr>" 
	print "<td>",elem['school'],"</td>"
	print "<td>",elem['time'],"</td>"
	print "<td>","""<a href=""",elem['link'],"""target="_blank">""",elem['title'],"</a>","</td>"
	print "</tr>"

print "</table>"
print "</div>"
print "</div>"
print "</body></html>"
