'''
作用： 对评论形成词云（模块缺失）
原教程：https://www.bilibili.com/video/BV1S44y1h7Da?spm_id_from=333.999.0.0
日期  2022年01月16日
'''
import jieba
import collections
import re
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 去除分词结果中的无用词汇
def deal_txt(seg_list_exact):
  stop={'用户','点赞数','评论','发表时间','今天','商场','中心','购物'}
  result_list = []
  with open('D:\数据\python 代码\能用的小东西\练习类\data.txt', encoding='utf-8') as f:
    con = f.readlines()
    stop_words = set()
    for i in con:
      i = i.replace("\n", "")  # 去掉读取每一行数据的\n
      stop_words.add(i)
  for word in seg_list_exact:
    # 设置停用词并去除单个词
    if word not in stop_words and len(word) > 1:
      result_list.append(word)
  return result_list

# 渲染词云
def render_cloud(word_counts_top100):
  word1 = WordCloud(init_opts=opts.InitOpts(width='1350px', height='750px', theme=ThemeType.MACARONS))
  word1.add('词频', data_pair=word_counts_top100,
      word_size_range=[15, 108], textstyle_opts=opts.TextStyleOpts(font_family='cursive'),
      shape=SymbolType.DIAMOND)
  word1.set_global_opts(title_opts=opts.TitleOpts('评论云图'),
            toolbox_opts=opts.ToolboxOpts(is_show=True, orient='vertical'),
            tooltip_opts=opts.TooltipOpts(is_show=True, background_color='red', border_color='yellow'))

  # 渲染在html页面上
  word1.render("D:\数据\python 代码\能用的小东西\实用类\weibo.html")

if __name__ == '__main__':
  # 读取弹幕文件
  with open('D:\数据\python 代码\能用的小东西\练习类\data.txt', encoding='utf-8') as f:
    data = f.read()

  # 文本预处理 去除一些无用的字符  只提取出中文出来
  new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)

  new_data = " ".join(new_data)
  # jieba分词将整句切成分词
  seg_list_exact = jieba.cut(new_data, cut_all=True)

  # 去掉无用词汇
  final_list = deal_txt(seg_list_exact)
  # 筛选后统计
  word_counts = collections.Counter(final_list)
  # 获取前100最高频的词
  word_counts_top100 = word_counts.most_common(100)
  # 可以打印出来看看统计的词频
  # print(word_counts_top100)
  # 渲染词云
  render_cloud(word_counts_top100)

