from glob import glob
import re

import nltk

i = 0
clean_reg = '<(.*?)>'
mini_dir = "/Users/hillmac/Documents/School/Winter-2018/Dight-360/W18_DIGHT360/assignments/Mini-CORE/"
function_words = ['\'m', '\'re', '\'ve', '--', '\'d', '\'ll', 'century', 'million', '^', 'n\'t', '-', '...', 'i', 'we', 'you', 'he', 'she', 'it', 'they', 'me', 'us', 'him', 'her', 'them', 'myself', 'ourselves', 'yourself', 'yourselves', 'herself', 'himself', 'itself', 'themselves', 'someone', 'anyone', 'noone', 'everyone', 'nobody', 'something', 'anything', 'nothing', 'everything', 'whoever', 'whatever', 'others', 'mine', 'ours', 'yours', 'hers', 'theirs', 'my', 'our', 'your', 'his', '``', "''", "'s", 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'its', 'their', 'one', 'first', 'second', 'third', 'once', 'this', 'these', 'that', 'those', 'a', 'an', 'the', 'all', 'alone', 'another', 'any', 'both', 'each', 'either', 'enough', 'very', 'few', 'former', 'latter', 'last', 'least', 'less', 'lot', 'lots', 'many', 'more', 'most', 'much', 'neither', 'next', 'none', 'only', 'other', 'several', 'same', 'some', 'such', 'top', 'whole', 'and', 'but', 'or', 'nor', 'although', 'as', 'because', 'if', 'while', 'however', 'whenever', 'wherever', 'whether', 'whyever', 'thereby', 'therein', 'thereupon', 'thereafter', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'again', 'also', 'besides', 'moreover', 'namely', 'furthermore', 'hence', 'so', 'therefore', 'thus', 'else', 'instead', 'otherwise', 'after', 'afterwards', 'before', 'meanwhile', 'then', 'until', 'anyhow', 'anyway', 'despite', 'even', 'nevertheless', 'though', 'yet', 'eg,' 'ie', 'per', 're', 'etc', 'about', 'above', 'across', 'against', 'along', 'among', 'amongst', 'amoungst', 'around', 'at', 'behind', 'below', 'beside', 'between', 'beyond', 'by', 'down', 'during', 'except', 'for', 'from', 'in', 'inside', 'into', 'near', 'of', 'off', 'on', 'onto', 'outside', 'over', 'since', 'than', 'thence', 'to', 'toward', 'towards', 'under', 'up', 'upon', 'through', 'thru', 'throughout', 'via', 'with', 'within', 'without', 'am', 'are', 'is', 'was', 'were', 'be', 'been', 'being', 'became', 'have', 'has', 'had', 'do', 'does', 'did', 'done', 'will', 'shall', 'may', 'can', 'cannot', 'would', 'could', 'should', 'might', 'ought', 'need', 'must', 'used', 'dare', 'yes', 'no', 'not', 'already', 'always', 'anywhere', 'beforehand', 'elsewhere', 'ever', 'everywhere', 'formerly', 'further', 'here', 'hereafter', 'hereabouts', 'hereinafter', 'heretofore', 'herewith', 'hereunder', 'hereby', 'herein', 'hereupon', 'indeed', 'latterly', 'mostly', 'never', 'nowhere', 'often', 'oftentimes', 'out', 'perhaps', 'somehow', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'still', 'there', 'thereabouts', 'thereof', 'thereon', 'together', 'well', 'almost', 'rather', 'too', 'very', 'who', 'whom', 'whose', 'what', 'which', 'when', 'where', 'why', 'how', 'whither', 'whence', '.', ',', '!', '?',':', ";", '[', ']', '(', ')', '\'', '/', '\"', 'I', 'We', 'You', 'He', 'She', 'It', 'They', 'Me', 'Us', 'Him', 'Her', 'Them', 'Myself', 'Ourselves', 'Yourself', 'Yourselves', 'Herself', 'Himself', 'Itself', 'Themselves', 'Someone', 'Anyone', 'Noone', 'Everyone', 'Nobody', 'Something', 'Anything', 'Nothing', 'Everything', 'Whoever', 'Whatever', 'Others', 'Mine', 'Ours', 'Yours', 'Hers', 'Theirs', 'My', 'Our', 'Your', 'His', 'Its', 'Their', 'One', 'First', 'Second', 'Third', 'Once', 'This', 'These', 'That', 'Those', 'A', 'An', 'The', 'All', 'Alone', 'Another', 'Any', 'Both', 'Each', 'Either', 'Enough', 'Very', 'Few', 'Former', 'Latter', 'Last', 'Least', 'Less', 'Lot', 'Lots', 'Many', 'More', 'Most', 'Much', 'Neither', 'Next', 'None', 'Only', 'Other', 'Several', 'Same', 'Some', 'Such', 'Top', 'Whole', 'And', 'But', 'Or', 'Nor', 'Although', 'As', 'Because', 'If', 'While', 'However', 'Whenever', 'Wherever', 'Whether', 'Whyever', 'Thereby', 'Therein', 'Thereupon', 'Thereafter', 'Whereafter', 'Whereas', 'Whereby', 'Wherein', 'Whereupon', 'Again', 'Also', 'Besides', 'Moreover', 'Namely', 'Furthermore', 'Hence', 'So', 'Therefore', 'Thus', 'Else', 'Instead', 'Otherwise', 'After', 'Afterwards', 'Before', 'Meanwhile', 'Then', 'Until', 'Anyhow', 'Anyway', 'Despite', 'Even', 'Nevertheless', 'Though', 'Yet', 'Eg,' 'Ie', 'Per', 'Re', 'Etc', 'About', 'Above', 'Across', 'Against', 'Along', 'Among', 'Amongst', 'Amoungst', 'Around', 'At', 'Behind', 'Below', 'Beside', 'Between', 'Beyond', 'By', 'Down', 'During', 'Except', 'For', 'From', 'In', 'Inside', 'Into', 'Near', 'Of', 'Off', 'On', 'Onto', 'Outside', 'Over', 'Since', 'Than', 'Thence', 'To', 'Toward', 'Towards', 'Under', 'Up', 'Upon', 'Through', 'Thru', 'Throughout', 'Via', 'With', 'Within', 'Without', 'Am', 'Are', 'Is', 'Was', 'Were', 'Be', 'Been', 'Being', 'Became', 'Have', 'Has', 'Had', 'Do', 'Does', 'Did', 'Done', 'Will', 'Shall', 'May', 'Can', 'Cannot', 'Would', 'Could', 'Should', 'Might', 'Ought', 'Need', 'Must', 'Used', 'Dare', 'Yes', 'No', 'Not', 'Already', 'Always', 'Anywhere', 'Beforehand', 'Elsewhere', 'Ever', 'Everywhere', 'Formerly', 'Further', 'Here', 'Hereafter', 'Hereabouts', 'Hereinafter', 'Heretofore', 'Herewith', 'Hereunder', 'Hereby', 'Herein', 'Hereupon', 'Indeed', 'Latterly', 'Mostly', 'Never', 'Nowhere', 'Often', 'Oftentimes', 'Out', 'Perhaps', 'Somehow', 'Sometime', 'Sometimes', 'Somewhat', 'Somewhere', 'Still', 'There', 'Thereabouts', 'Thereof', 'Thereon', 'Together', 'Well', 'Almost', 'Rather', 'Too', 'Very', 'Who', 'Whom', 'Whose', 'What', 'Which', 'When', 'Where', 'Why', 'How', 'Whither', 'Whence']
list_nums = [str(x) for x in range(5000 + 1)]
list_registers = [('IN', 'Informational (Wiki)'), ('IP', 'Informational Persuasion'), ('SP', 'Interview Transcripts'), ('LY', 'Song Lyrics'), ('NA', 'News Reports'), ('OP', 'Opinion Blogs')]

for each in list_nums:
    function_words.append(each)
set_function_words = set(function_words)

for a, b in list_registers:
    fdist = nltk.FreqDist()
    for filename in glob(mini_dir + '*.txt'):
        register = filename.split('+')[1]
        if register == a:
            with open(filename) as input_file:
                i += 1
                print(i)
                clean_file = re.sub(clean_reg, '', input_file.read(), flags=re.DOTALL)
                clean_string = ''.join(clean_file)
                clean_string_lower = clean_string.lower()
                input_sents = nltk.sent_tokenize(clean_string_lower)
                for sentence in input_sents:
                    input_words = nltk.word_tokenize(sentence)
                    fdist.update([word for word in input_words if word not in set_function_words])
    with open('frequency_distribs_' + a + '.txt', 'w') as file_fdist:
        print(b, file=file_fdist)
        for key, value in fdist.most_common():
            print((key, value), file=file_fdist)

#Perhaps the most interesting thing from the word count analysis was that the most frequent word in Interview Transcripts AND Song Lyrics was 'like'. Like seriously?
#The song lyrics and the opinion blogs used a lot of the same simple nouns and adjectives. News Reports says names and the word 'said' way more than other groups.
#The Wiki articles love the word state (plural AND singular) and lot of other nouns that don't appear much in the other registers.
#Interview Trans, Opinion Blogs and News Reports are all fairly similar while the two Informational types are closer. Song lyrics appears to be the most unique.