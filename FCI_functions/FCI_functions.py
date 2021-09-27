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
    corr_ans = ['C', 'A' , 'C', 'E', 'B', 'B', 'B', 'B' , 'E', 'A', 'D', 'B', 'D', 'D', 'A', 'A', 'B', 'B', 'E', 'D', 
            'E', 'B', 'B', 'A', 'C', 'E', 'C', 'E', 'B', 'C']
    scores = []
    num_students = len(df.index)
    for j in range(1, 31):
        score = 0
        string = "PRE Q"+ str(j)
        for i in range(1,num_students):
                if df[string][i]==corr_ans[j-1]:
                    score+=1
        scores.append(score)
        
    return (scores)