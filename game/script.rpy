label start:

    "On our first date, Sylvia gave me a houseplant."

    show plant at truecenter

    "I'm not really the kind of person who likes plants. I had mixed feelings about her gift."

    "Nonetheless, I thought it was a cute gift. In a way that made me like her more."

    "I was already fond of her and I wanted to do something so that she would feel the same way towards me."

    "I gladly accepted the plant with open arms and made a commitment to tend to it as best as I can."

    hide plant
    show sylvia

    "Sylvia was different from the other girls."

    "Just from the fact that she gave a plant on our first date."

    "But that's what makes her special."

    "Others might not like this kind of strange quirk."

    "But I'm not like those others. Her peculiar habits made me like her more."

    hide sylvia
    scene class

    "We were classmates at first period. That was the only time we would really meet."

    scene vendingmachines

    "One time during vacant hours I saw her near the vending machines."

    "She was observing something at the floor. Me being curious, I decided to walk up to her and take a closer look."

    "I saw her watching a mantis."

    show mantis at truecenter

    "Every person walking by ignored the mantis but she paused and examined it."

    hide mantis
    show sylvia smile

    "She eventually acknowledged me and looked at me. She gave me a lovely smile and said..."

    "\"The most stunning things come from nature, thus you should just calm down and concentrate.\""

    "I realized then that I needed to get to know her better."

    "I brought up our classes when we first spoke. I invited her out because I thought we would get along."

    "She happily accepted."

    scene mall
    show sylvia

    "Later on that day, we met. She then had the idea for the little plant."

    scene apartment
    hide sylvia

    "I drove home holding the plant like a baby. I placed the plant next to my apartment's door so I wouldn't forget about it."

    "It was dazzling the day I brought it inside, just like a dog discovering a new environment. It nearly had the impression of gleaming."

    scene class

    "I didn't run into her the day after we went out. She was someone I missed and yearned to see soon."

    show phone at truecenter

    "I texted her to express my appreciation for the gift and my desire to speak with her again."

    "She stayed silent."

    "My heart started to gradually grow cold."

    "Every few minutes, I glanced at the phone to see if she had picked up, but I was unsuccessful."

    scene apartment
    hide phone
    show plant at truecenter

    "I took note of the tiny plant by the entrance when I returned to the apartment."

    "It seemed a little worse off than the first day."

    "Who knows? Perhaps it was the new environment." 
    
    "I questioned whether I needed to water it."

menu:

    "Water the plant":

        $ watered = True
        jump watered

    "Don't do anything":

        $ watered = False
        jump unwatered

label watered:

    "To be on the safe side, I gave it a good watering. The water was happily absorbed by the soil."

    hide plant
    show phone at truecenter

    "Just to make sure she was alright, I called Sylvia."

    "The phone didn't get her attention. I was a little anxious."

    "Perhaps she didn't want to speak with me? I was clueless."

    "The previous day, I felt we were in positive spirits."

    hide phone

    "Thoughts were running through my head as I went to bed."

    jump chapter1

label unwatered:
        
    "I assumed I was worrying excessively. For the time being, I let it be."

    hide plant

    "I made the decision to temporarily leave Sylvia alone. Maybe she was unable to respond."
    
    "I tried to unwind as I went to sleep. She was still on my mind."

label chapter1:

    show plant at truecenter

    "The following day, I looked at the plant before leaving for the lesson."

    "It seemed okay. Not much has changed from yesterday."

    "I wasn't sure what to make of it, but I had to leave because I was running late for the lesson."

    scene class
    hide plant
    show sylvia

    "There, in the class, was Sylvia. As soon as our eyes connected, I felt a tiny drop in my heart."
    
    show sylvia smile

    "But when she smiled at me, I started to feel more at ease."

    hide sylvia

    "After the lesson was over, I approached her and we chatted for a while. She claimed that she and her mother had a fight."

    show sylvia sad

    "She had a terrible evening and needed some alone time."

    "If she would like to talk, I suggested that perhaps I could be of help."

    "She said she wanted to forget about it and she seemed a little irritated." 
    
    "I asked her about going out again because I wanted to give her a distraction from her problems."

    show sylvia smile

    "She smiled warmly and accepted my offer."

    hide sylvia

    "I waited till the afternoon, enthusiastic for the new date."

    scene cafeteria

    "This time, we went to the cafeteria."

    hide sylvia
    show icecream at truecenter

    "We decided to eat ice cream there."

    "Even the manner she ate it was distinctive to her."

    "She took a spoonful and dropped it in her mouth, and let it melt there for the good part of a minute, making all sort of faces and comments about the wonderful taste."

    "I admired her way of eating with each spoonful of ice cream. Probably a bit too much."

    hide icecream

    show sylvia smile

    "She realized what she was doing and she smiled. But it was probably not because she liked it but out of politeness."

    "We discussed a wide range of topics. Everything excluding the family."

    "When we started discussing our hobbies, things started to go south."

    "I told her I like playing video games."

    show sylvia neutral

    "She appeared to be a little hesitant after that. She closed up, and everything I said after that, she listened to coldly."

    "That sort of response surprised me. It seemed a little strange to me."

    hide sylvia

    "With a little bit of cold between us, we parted ways." 

    scene apartment
    
    "I was preoccupied with her response as I returned home."
    
    show plant at truecenter

    "When I arrived, I observed the plant was looking much worse today."

    "The leaves dropped down, and it seemed like it was not in excellent shape."

    "I questioned whether I needed to fertilize it."

menu:

    "Fertilize the plant":

        $ fertilized = True
        jump fertilized

    "Don't do anything":

        $ fertilized = False
        jump unfertilized

label fertilized:

    "It might have needed the fertilizer so I chose to fertilize it."

    hide plant
    show phone at truecenter

    "I gave Sylvia a call. She answered this time."

    "I began to wonder if there really was something she didn't want to tell me and why that is the case."

    "I could see she was hesitant about it but I really wanted to know."

    "She started crying after a few minutes of contrast."

    "I heard her weeping on the other end of the call."

    "She apologized in such a pathetic tone that I immediately melted."

    "She began speaking with me about his ex, a man who played professional video games."

    "He saw her as an obstacle in his improvement to playing profesionally so he left her."

    "As expected, she was devastated. Her reaction of that afternoon is understandable, under this light."

    "I spoke to her softly in an effort to keep her spirits high. She appeared to calm down."

    "She slept soundly after chatting on for hours. Her snoring could be heard clearly on my end."

    hide phone

    "I finally ended the call and slept free of worries."

    jump chapter2

label unfertilized:

    "Perhaps it was just simply adjusting to the new surroudings. I thought it didn't really acquire any."

    hide plant

    "I feared that she would think I was being obnoxious so I didn't continue my initial thought to call her up."

    "I quickly went to bed."

    "My anxiety made it difficult for me to sleep properly. Thoughts about what happened that time kept appearing in my head."

label chapter2:

    scene class
    show sylvia

    "I spend a lot of my time the following week with Sylvia. We had lunch together, discussing about lessons."

    "I noticed that I laughed a lot whenever I was with her. I liked her sense of humor."

    "I could feel my feelings for her developing over time."

    "At the end of the month was the crucial day."

    "I pretty much had nothing to do since it was a Saturday at the time."

    "Since the previous week, we hadn't run into each other outside of the classroom. So I texted her about something."

    "Sylvia and I exchanged messages to see if we wanted to go somewhere."

    show sylvia smile

    "She said she would be delighted to do so."

    "I was overjoyed. My heart was filled with happiness."

    scene park
    show sylvia

    "Soon after, Sylvia and I met."

    "She seemed more beautiful than usual."

    show sylvia blush

    "I told her she looked amazing. She got flustered and thanked me after."

    "I went in for a hug and my heart started beating faster."

    "My body experienced her touch as nothing less than an electric shock."

    show sylvia smile

    "As I was moving away from her, I looked her in the eyes and saw her smiling."

    "We talked extensively about ourselves and our pasts while out for a stroll."

    "We became accustomed to talking to one another and began to feel a connection."

    "A ray of light that had just pierced the trees struck her in the face."

    "I still remember that moment vividly."

    "In that moment, only one thought occupied my mind."

    show sylvia

    "I had never seen a girl more lovely than she was."

    "I experienced a spark in my heart at that precise moment."

    "She was the definite woman I'd spend my life with."

    "She was moving in front of me by a few steps."

    if watered and fertilized:
        jump ending1
    elif watered and not fertilized:
        jump ending2
    elif not watered and fertilized:
        jump ending3
    else:
        jump ending4

label ending1:

    "She turned as I called to her."

    "I took her arm and drew her close to me, enjoying the warmth of her body on mine."

    hide sylvia

    "We kissed each other."

    "I felt her astonishment as tightness on her lips, but soon her mouth turned soft, and we embraced in a passionate kiss."

    "I have no idea how long we were kissing."

    "All sense of time and space blurred."

    "I knew I loved her when we parted ways. She also understood this."

    "Her eyes showed it to me."

    "We both wanted to take our relationship further."

    scene black

    "5 years after graduating college, we were still going strong."

    "So we decided to get married."

    "It was only a matter of time, given that our love for each other was unwavering."

    "After our marriage, I prepared a special gift for her to celebrate."

    "I gave her a little plant, similar to the first gift she gave to me."

    "I couldn't figure out what her reaction was. She seemed like she was laughing and crying at the same time."

    "She said it was kind of cheesy but she still appreciated it."

    show plant at truecenter

    "Regardless, we put our little plants together in our new home. Symbolizing our relationship together."

    "End (1/4)"

    return

label ending2:

    "I wanted to ask her a question. She turned around"

    show sylvia

    "My heart was racing. The words in my head were not coming out."

    "After mustering up the courage I need, I spoke."

    "I asked if we could continue this relationship forever."

    show sylvia smile

    "She laughed, explaining as if that wasn't the case already."

    "We were already fond of each other."

    "But there was still a lingering feeling that maybe this wasn't mutual."

    "I knew I loved her and it feels me with happiness that she also feels the same."

    "While we were together at the time, it created the best moments of my life."

    scene black
    hide sylvia

    "3 years our relationship lasted. The passion we once had was slowly fading and we both knew it."

    "We decided to go our separate paths. We both knew that we were too different to get married."

    show plant at truecenter

    "About her plant, I still take care of it."

    "I look at it whenever I'm feeling down."

    "It reminds me of her beautiful smile, cheering me up."

    "Even if it ended bitterly, I'm still thankful for all the memories and experiences."

    hide plant

    "End (2/4)"

    return

label ending3:

    "I felt her beauty's power as I gazed upon her."

    "I felt helpless right there."

    "Fearing I would destroy this beautiful moment, I was frozen, unable to do anything."

    "But we kept on walking until we said our goodbyes."

    hide sylvia

    "I felt an emptiness in my heart."

    scene apartment

    "That evening when I returned home, I had a broken feeling inside."
    
    "An expanding void was manifesting between us, and I couldn't fill it."

    "I blew my opportunity."

    "I rushed to my bed and broke down."

    "I was tormented by the thought of what might have been for us."

    "What would have happened if I had the courage to act that day?"

    "The idea of a present unfulfilled devastated me."

    scene class
    show sylvia

    "After a few weeks, she informed me that she was seeing someone else."

    show sylvia smile

    "She was overjoyed. The same joy I experienced from her in that summer day."

    "Out of politeness, I told her I was happy for her."

    "It was agonizing thinking about my dreams with her became a reality with someone else."

    "Nevertheless, we still talked as friends."

    "Nothing more than that."

    hide sylvia

    "I met her boyfriend. He seems like he would be good for her."

    scene black
    show plant at truecenter

    "About the little plant I received from her, it unfortunately died."

    "A fungal infection ate up the whole plant."

    hide plant

    "So I threw it away. As I did it, I felt a heavy weight on my chest."

    "The feelings I once had for her were all coming back."

    "And then vanished right after."

    "I accepted the fact that Sylvia was a good friend."

    "And that I needed to move on."

    "End (3/4)"

    return

label ending4:

    "I called out her name and she turned around and looked at me."

    show sylvia

    "I got closer to her and held her hand."

    "I tried to go for a kiss."

    show sylvia sad

    "She moved away from me."

    "I felt a sharp pain in my heart."

    "The thoughts of us being together forever, was all a delusion I made up inside my head."

    "I backed away from her, ashamed."

    "I laughed nervously, pretending like nothing happened."

    show sylvia neutral

    "She gave a tepid smile while trying averting her eyes."

    "The mood suddenly shifted from lively to akward."

    hide sylvia

    "We set out on foot in silence."

    "I felt as though I had ruined something beautiful."

    "We could not look at each other in the eyes."

    "The distance between us became increasingly cold."

    "The cold silence was deafening. Shortly after, Sylvia said she had to go."

    "She said that she needs to study. I could only nod my head. No words could come out of my mouth."

    "As I saw her walk into the distance, I felt disenchanted."

    "Although I wanted her to be mine, I suppose fate had other plans for the two of us."

    scene apartment
    show plant at truecenter

    "I went home and noticed the plant she gave to me."

    "The pain only got worse."

    "My love for her was evident when I saw her lovely smile and she wouldn't accept it."

    "I accepted the plant as her gift, but she wouldn't accept my love in return."

    "I decided to give the plant to a friend of mine so it could get better treatment."

    hide plant

    "It reminded me of my regrets even though I became attached to it."
    
    "It was too much for me to handle."

    "Sylvia and I were still in touch. She tried to still be friends with me but I couldn't bring myself to do it."

    show phone at truecenter

    "Later, she revealed to me that she was dating another man."

    "All the memories of us came rushing in my head. For me, it was too much to bear."

    hide phone

    "After that day, I cut off all contact with her."

    "She tried contacting me but I ignored her."

    "Life eventually got the better of me, and I resumed my normal routine."

    "I finally got to move on."

    "End (4/4)"

    return