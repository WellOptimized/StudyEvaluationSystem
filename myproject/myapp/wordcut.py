import nltk
import jieba
# jieba.load_userdict('/home/mingchao/lcs_data/comment_jieba_add_word.txt')
import jieba.posseg as pseg
def leaves(tree):
    for subtree in tree.subtrees(filter=lambda t: t.label()=='NP'):
        yield subtree.leaves()
def extract_asp_by_grammar(text):     
    # text = "因为这个风格蛮喜欢的,加上TapTap的推荐就下载来玩了,bgm挺好的游戏（开着bgm写的评论）,然后游戏体验相当棒了"
    words = pseg.cut(text)
    sent_tags = [(x, y) for x, y in words]
    print(sent_tags)
    # NP(名词短语块) DT(限定词) JJ(形容词) NN(名词)
    # 名词名词，或者名词形容词
    # grammar = "NP: {<n>{2,4}}"

    grammar = r"""
                NP: 
                    {<v><n><zg>*<d>*(<a>|<ad>|<ag>|<an>)+}
                    {<n>+<zg>*<d>*(<a>|<ad>|<ag>|<an>)+}
                    {<v>+<zg>*<d>*(<a>|<ad>|<ag>|<an>)+}  
                    {<v>+<zg>*<d>*<n>+}  

                """
    # 进行分块
    cp = nltk.RegexpParser(grammar)
    tree = cp.parse(sent_tags)
    aspects = [[w for w,t in leaf] for leaf in leaves(tree)]
    return [''.join(asp) for asp in aspects]

if __name__ == "__main__":
    # execute only if run as a script
    # text = "因为这个风格蛮喜欢的,加上TapTap的推荐就下载来玩了,bgm挺好的游戏（开着bgm写的评论）,然后游戏体验相当棒了"
    text = "上课内容很充实，作业设置很合理，速度正好。上课上课上课上课充实充实充实充实充实充实充实充实充实充实充实"


    print(extract_asp_by_grammar(text))