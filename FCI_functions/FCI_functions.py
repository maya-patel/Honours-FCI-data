def calculate_pre_score(student):
    corr_ans = ['C', 'A' , 'C', 'E', 'B', 'B', 'B', 'B' , 'E', 'A', 'D', 'B', 'D', 'D', 'A', 'A', 'B', 'B', 'E', 'D', 
            'E', 'B', 'B', 'A', 'C', 'E', 'C', 'E', 'B', 'C']
    student_pre = [] 
    score = 0
    for i in range(1,31):
        string = "PRE Q"+ str(i)
        if string in student:
            if student[string]==corr_ans[i-1]:
                score+=1
            
    return (score)

def calculate_post_score(student):
    corr_ans = ['C', 'A' , 'C', 'E', 'B', 'B', 'B', 'B' , 'E', 'A', 'D', 'B', 'D', 'D', 'A', 'A', 'B', 'B', 'E', 'D', 
            'E', 'B', 'B', 'A', 'C', 'E', 'C', 'E', 'B', 'C']
    student_pre = [] 
    score = 0
    for i in range(1,31):
        string = "POST Q"+ str(i)
        if string in student:
            if student[string]==corr_ans[i-1]:
                score+=1
            
    return (score)

def calculate_question_score_post(df):
    num = len(df.index)
    scores = [
    df["POST Q1"].value_counts().C/num,
    df["POST Q2"].value_counts().A/num,
    df["POST Q3"].value_counts().C/num,
    df["POST Q4"].value_counts().E/num,
    df["POST Q5"].value_counts().B/num,
    df["POST Q6"].value_counts().B/num,
    df["POST Q7"].value_counts().B/num,
    df["POST Q8"].value_counts().B/num,
    df["POST Q9"].value_counts().E/num,
    df["POST Q10"].value_counts().A/num,
    df["POST Q11"].value_counts().D/num,
    df["POST Q12"].value_counts().B/num,
    df["POST Q13"].value_counts().D/num,
    df["POST Q14"].value_counts().D/num,
    df["POST Q15"].value_counts().A/num,
    df["POST Q16"].value_counts().A/num,
    df["POST Q17"].value_counts().B/num,
    df["POST Q18"].value_counts().B/num,
    df["POST Q19"].value_counts().E/num,
    df["POST Q20"].value_counts().D/num,
    df["POST Q21"].value_counts().E/num,
    df["POST Q22"].value_counts().B/num,
    df["POST Q23"].value_counts().B/num,
    df["POST Q24"].value_counts().A/num,
    df["POST Q25"].value_counts().C/num,
    df["POST Q26"].value_counts().E/num,
    df["POST Q27"].value_counts().C/num,
    df["POST Q28"].value_counts().E/num,
    df["POST Q29"].value_counts().B/num,
    df["POST Q30"].value_counts().C/num]
    return scores

def calculate_question_score_pre(df):
    num = len(df.index)
    scores = [
    df["PRE Q1"].value_counts().C/num,
    df["PRE Q2"].value_counts().A/num,
    df["PRE Q3"].value_counts().C/num,
    df["PRE Q4"].value_counts().E/num,
    df["PRE Q5"].value_counts().B/num,
    df["PRE Q6"].value_counts().B/num,
    df["PRE Q7"].value_counts().B/num,
    df["PRE Q8"].value_counts().B/num,
    df["PRE Q9"].value_counts().E/num,
    df["PRE Q10"].value_counts().A/num,
    df["PRE Q11"].value_counts().D/num,
    df["PRE Q12"].value_counts().B/num,
    df["PRE Q13"].value_counts().D/num,
    df["PRE Q14"].value_counts().D/num,
    df["PRE Q15"].value_counts().A/num,
    df["PRE Q16"].value_counts().A/num,
    df["PRE Q17"].value_counts().B/num,
    df["PRE Q18"].value_counts().B/num,
    df["PRE Q19"].value_counts().E/num,
    df["PRE Q20"].value_counts().D/num,
    df["PRE Q21"].value_counts().E/num,
    df["PRE Q22"].value_counts().B/num,
    df["PRE Q23"].value_counts().B/num,
    df["PRE Q24"].value_counts().A/num,
    df["PRE Q25"].value_counts().C/num,
    df["PRE Q26"].value_counts().E/num,
    df["PRE Q27"].value_counts().C/num,
    df["PRE Q28"].value_counts().E/num,
    df["PRE Q29"].value_counts().B/num,
    df["PRE Q30"].value_counts().C/num]
    return scores


def calculate_pre_score_2020(student):
    corr_ans = [3,5,2,1,2,2,3,4,3,1,3,3,5,5,4,4,4,1,3,4,4,2,5,5,2,4,2,2,5,2]
    pre = [] 
    for i in range (1, 31):
        string = "PRE Q" + str(i)
        pre.append(string)
    score = 0
    for i in range(1,31):
            if student[pre[i-1]]==corr_ans[i-1]:
                score+=1
            
    return (score)


def calculate_post_score_2020(student):
    corr_ans = [3,5,2,1,2,2,3,4,3,1,3,3,5,5,4,4,4,1,3,4,4,2,5,5,2,4,2,2,5,2]
    pre = [] 
    for i in range (1, 31):
        string = "POST Q" + str(i)
        pre.append(string)
    score = 0
    for i in range(1,31):
            if student[pre[i-1]]==corr_ans[i-1]:
                score+=1
            
    return (score)

def calculate_question_score_pre_2020(df):
    num = len(df.index)
    scores = [
    df["PRE Q1"].value_counts().loc[3.0]/num,
    df["PRE Q24"].value_counts().loc[5.0]/num,
    df["PRE Q25"].value_counts().loc[2.0]/num,
    df["PRE Q26"].value_counts().loc[1.0]/num,
    df["PRE Q27"].value_counts().loc[2.0]/num,
    df["PRE Q28"].value_counts().loc[2.0]/num,
    df["PRE Q29"].value_counts().loc[3.0]/num,
    df["PRE Q30"].value_counts().loc[4.0]/num,
    df["PRE Q31"].value_counts().loc[3.0]/num,
    df["PRE Q32"].value_counts().loc[1.0]/num,
    df["PRE Q33"].value_counts().loc[3.0]/num,
    df["PRE Q34"].value_counts().loc[3.0]/num,
    df["PRE Q35"].value_counts().loc[5.0]/num,
    df["PRE Q36"].value_counts().loc[5.0]/num,
    df["PRE Q37"].value_counts().loc[4.0]/num,
    df["PRE Q38"].value_counts().loc[4.0]/num,
    df["PRE Q39"].value_counts().loc[4.0]/num,
    df["PRE Q40"].value_counts().loc[1.0]/num,
    df["PRE Q41"].value_counts().loc[3.0]/num,
    df["PRE Q42"].value_counts().loc[4.0]/num,
    df["PRE Q43"].value_counts().loc[4.0]/num,
    df["PRE Q44"].value_counts().loc[2.0]/num,
    df["PRE Q45"].value_counts().loc[5.0]/num,
    df["PRE Q46"].value_counts().loc[5.0]/num,
    df["PRE Q47"].value_counts().loc[2.0]/num,
    df["PRE Q48"].value_counts().loc[4.0]/num,
    df["PRE Q49"].value_counts().loc[2.0]/num,
    df["PRE Q50"].value_counts().loc[2.0]/num,
    df["PRE Q51"].value_counts().loc[5.0]/num,
    df["PRE Q52"].value_counts().loc[2.0]/num]
    return scores

def calculate_question_score_post_2020(df):
    num = len(df.index)
    scores = [
    df["POST Q1"].value_counts().loc[3.0]/num,    
    df["POST Q35"].value_counts().loc[5.0]/num,
    df["POST Q36"].value_counts().loc[2.0]/num,
    df["POST Q37"].value_counts().loc[1.0]/num,
    df["POST Q38"].value_counts().loc[2.0]/num,
    df["POST Q39"].value_counts().loc[2.0]/num,
    df["POST Q40"].value_counts().loc[3.0]/num,
    df["POST Q41"].value_counts().loc[4.0]/num,
    df["POST Q42"].value_counts().loc[3.0]/num,
    df["POST Q43"].value_counts().loc[1.0]/num,
    df["POST Q44"].value_counts().loc[3.0]/num,
    df["POST Q45"].value_counts().loc[3.0]/num,
    df["POST Q46"].value_counts().loc[5.0]/num,
    df["POST Q47"].value_counts().loc[5.0]/num,
    df["POST Q48"].value_counts().loc[4.0]/num,
    df["POST Q49"].value_counts().loc[4.0]/num,
    df["POST Q50"].value_counts().loc[4.0]/num,
    df["POST Q51"].value_counts().loc[1.0]/num,
    df["POST Q52"].value_counts().loc[3.0]/num,
    df["POST Q53"].value_counts().loc[4.0]/num,
    df["POST Q54"].value_counts().loc[4.0]/num,
    df["POST Q55"].value_counts().loc[2.0]/num,
    df["POST Q56"].value_counts().loc[5.0]/num,
    df["POST Q57"].value_counts().loc[5.0]/num,
    df["POST Q58"].value_counts().loc[2.0]/num,
    df["POST Q59"].value_counts().loc[4.0]/num,
    df["POST Q60"].value_counts().loc[2.0]/num,
    df["POST Q61"].value_counts().loc[2.0]/num,
    df["POST Q62"].value_counts().loc[5.0]/num,
    df["POST Q63"].value_counts().loc[2.0]/num]
    return scores


