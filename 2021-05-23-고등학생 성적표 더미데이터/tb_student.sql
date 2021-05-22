create table tb_student (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(10) NOT NULL,
entrance INT NOT NULL,
school_id INT,
PRIMARY KEY (id),
FOREIGN KEY (school_id) REFERENCES tb_school (id));