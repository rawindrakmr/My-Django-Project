from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'newsapp/index.html')

def moviesinfo(request):
    head_msg='Latest Movies Information'
    msg1='Amidst too many conspiracy theories, a friend has said that Disha Salian had a very emotional moment which led her to jumping off from the bedroom window'
    msg2='Sushant Singh Rajput suicide: Rhea Chakraborty has released a page from a diary where the late actor expresses gratitude for the presence of her and her folks in his life'
    msg3='Sushant Singh Rajput Death: Ankita Lokhande has shared a picture of the late actor\'s mother on her social media saying she believed Sushant was with his mom'
    msg4='#Warriors4SSR: Shweta Singh Kirti, Sushant Singh Rajput\'s sister has shared pics and videos of his billboards being put up in California'
    dict_={'head_msg':head_msg, 'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'newsapp/news.html', context=dict_)
def sportinfo(request):
    head_msg='Latest Sport Information'
    msg1='Yuzvendra Chahal and choreographer Dhanashree Verma made their relationship official on Saturday, sharing pictures from the Roka ceremony.'
    msg2='UEFA Champions League 2020, Barcelona vs Napoli, Bayern vs Chelsea Football Live Score Streaming: Bayern will be considered favourites against Chelsea, courtesy to the 3-0 victory in the first-leg which was played in February.'
    msg3='Jhulan, who too is 37 like Mithali, also wants to be there in New Zealand 18 months from now but says her fitness and performance in the run up to the event will decide that.'
    msg4='Shoaib Akhtar recalls how a 25-year-old MS Dhoni had frustrated him so much that he was forced to bowl his first intentional beamer at the batsman. He said he apologized to Dhoni after the delivery.'
    dict_={'head_msg':head_msg, 'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'newsapp/news.html', context=dict_)
    
def politicsinfo(request):
    head_msg='Latest Politics Information'
    msg1='The NDA government in Maharashtra is mulling over to reduce \'excess\' water supply for agriculture to Baramati, the hometown of NCP chief Sharad Pawar, as it believes that the area has been getting more water due to political influence.'
    msg2='Known for his administrative prowess and innovative approach in addressing issues, Gadkari has been instrumental in pushing infrastructure development and reviving projects stuck for many years.'
    msg3='The opposition led by the Congress has been accusing the government of benefiting Anil Ambani \'s Reliance Defence Ltd. from the Rafale deal. The government and Reliance Defence have dismissed all the allegations as false.'
    msg4='The BJP is trying to expand its influence in the southern state, which has been dominated by the CPI(M)-led Left Front and Congress-headed United Democratic Front for decades.'
    dict_={'head_msg':head_msg, 'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'newsapp/news.html', context=dict_)
    

