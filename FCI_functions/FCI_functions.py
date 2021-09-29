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
            
    return (score*100/30)

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
            
    return (score*100/30)

def calculate_question_score_post(df):
    corr_ans = ['C', 'A' , 'C', 'E', 'B', 'B', 'B', 'B' , 'E', 'A', 'D', 'B', 'D', 'D', 'A', 'A', 'B', 'B', 'E', 'D', 
            'E', 'B', 'B', 'A', 'C', 'E', 'C', 'E', 'B', 'C']
    scores = []
    num_students = len(df.index)
    for j in range(1, 31):
        score = 0
        string = "POST Q"+ str(j)
        for i in range(1,num_students):
                if df[string][i]==corr_ans[j-1]:
                    score+=1
        scores.append(score)
        
    return (scores)

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
