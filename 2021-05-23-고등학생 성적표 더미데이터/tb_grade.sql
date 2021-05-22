create table tb_grade (
student_id INT,
year INT NOT NULL,
semester INT NOT NULL,
subject VARCHAR(10) NOT NULL,
grade INT NOT NULL,
FOREIGN KEY (student_id) REFERENCES tb_student (id));