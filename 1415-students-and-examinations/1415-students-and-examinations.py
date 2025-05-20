import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
     # Perform a cross join between students and subjects
    all_combinations = students.merge(subjects, how='cross')

    # Count the number of examinations per student per subject
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    # Left join the counts to the full student-subject combinations
    result = all_combinations.merge(exam_counts, on=['student_id', 'subject_name'], how='left')

    # Fill NaN exam counts with 0
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)

    # Sort the result as per expected output
    result = result.sort_values(by=['student_id', 'subject_name'])

    return result

    