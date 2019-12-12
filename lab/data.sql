CREATE TABLE stu_details(
	reg_no int,
	stu_name varchar(20),
	DOB date,
	address varchar(20),
	city varchar(20),
	primary key(reg_no)
);

CREATE TABLE mark_details(
	reg_no int primary key,
	mark1 int default 0,
	mark2 int default 0,
	mark3 int default 0,
	total int default 0
);

ALTER TABLE mark_details
ADD COLUMN average long;

INSERT INTO stu_details values (001,'a','2000-5-12','road 1','city 1');
INSERT INTO stu_details values (002,'b','2001-6-12','road 2','city 2');
INSERT INTO stu_details values (003,'c','2004-5-12','road 3','city 3');
INSERT INTO stu_details values (004,'d','2004-4-12','road 4','city 4');
INSERT INTO stu_details values (005,'e','2005-2-12','road 5','city 5');
INSERT INTO stu_details values (006,'f','2007-7-12','road 6','city 6');
INSERT INTO stu_details values (007,'d','2004-4-12','road 7','city 7');
INSERT INTO stu_details values (008,'e','2005-2-12','road 8','city 8');
INSERT INTO stu_details values (009,'f','2007-7-12','road 9','city 9');
INSERT INTO stu_details values (010,'d','2004-4-12','road 10','city 10');
INSERT INTO stu_details values (011,'e','2005-2-12','road 11','city 11');
INSERT INTO stu_details values (012,'f','2007-7-12','road 12','city 12');


select 12-month(DOB) + (2019-year(DOB))*12 + 12 from stu_details;

ALTER TABLE stu_details DROP COLUMN address;




CREATE TABLE emp_details(
	emp_no int primary key,
	emp_name varchar(20),
	DOB date,
	address varchar(20),
	doj date,
	mobile_no varchar(20),
	dept_no int,
	salary int
);

INSERT INTO emp_details values(001,'a','2002-6-3','a','2008-5-6','8521476',002,254);
INSERT INTO emp_details values(002,'b','2002-6-3','b','2008-5-6','5214752',004,254);
INSERT INTO emp_details values(003,'c','2002-6-3','c','2008-5-6','8521476',001,234);
INSERT INTO emp_details values(004,'d','2002-6-3','d','2008-5-6','8521476',006,214);
INSERT INTO emp_details values(005,'e','2002-6-3','e','2008-5-6','5214752',008,274);
INSERT INTO emp_details values(006,'f','2002-6-3','f','2008-5-6','8521476',011,2554);
INSERT INTO emp_details values(007,'g','2002-6-3','g','2008-5-6','8521476',002,214);
INSERT INTO emp_details values(008,'h','2002-6-3','h','2008-5-6','2415789',004,454);
INSERT INTO emp_details values(009,'i','2002-6-3','i','2008-5-6','8521476',003,54);
INSERT INTO emp_details values(010,'j','2002-6-3','j','2008-5-6','2145874',005,24);
INSERT INTO emp_details values(011,'k','2002-6-3','k','2008-5-6','8521476',009,4);


CREATE TABLE dept_details(
	dept_no int primary key,
	dept_name varchar(20),
	location varchar(20)
);

INSERT INTO dept_details values(001,'A','Aa');
INSERT INTO dept_details values(002,'B','Ba');
INSERT INTO dept_details values(003,'C','Ca');
INSERT INTO dept_details values(004,'D','Da');
INSERT INTO dept_details values(005,'E','Ea');
INSERT INTO dept_details values(006,'F','Fa');
INSERT INTO dept_details values(007,'G','Ga');
INSERT INTO dept_details values(008,'H','Ha');
INSERT INTO dept_details values(009,'I','Ia');
INSERT INTO dept_details values(010,'J','Ja');
INSERT INTO dept_details values(011,'K','Ka');

select 12-month(doj) + (2019-year(doj))*12 + 12 from emp_details;

ALTER TABLE emp_details INSERT COLUMN primary key(emp_no);

CREATE VIEW showEmpDetails as 
select emp_no,emp_name from emp_details;

SELECT dept_no FROM dept_details WHERE dept_no NOT IN (SELECT dept_no FROM emp_details);

DELETE FROM dept_details;

DESCRIBE emp_details;

SELECT emp_name FROM emp_details ORDER BY salary DESC LIMIT 2;

CREATE TABLE customer(
	cust_id int primary key,
	cust_name varchar(20),
	addr varchar(20),
	ph_no varchar(20),
	pan_no varchar(20)
);

CREATE TABLE loan(
	loan_id int primary key,
	amount int,
	intrest int,
	cust_id int,
	branch int
);

INSERT INTO customer VALUES (001,'a','a',00101,12501);
INSERT INTO customer VALUES (002,'b','b',00102,12502);
INSERT INTO customer VALUES (003,'c','c',00103,12503);
INSERT INTO customer VALUES (004,'d','d',00104,12504);
INSERT INTO customer VALUES (005,'e','e',00105,12505);
INSERT INTO customer VALUES (006,'f','f',00106,12506);
INSERT INTO customer VALUES (007,'g','g',00107,12507);
INSERT INTO customer VALUES (008,'h','h',00108,12508);
INSERT INTO customer VALUES (009,'i','i',00109,12509);
INSERT INTO customer VALUES (010,'j','j',00110,12510);
INSERT INTO customer VALUES (011,'k','k',00111,12511);
INSERT INTO customer VALUES (012,'l','l',00112,12512);
INSERT INTO customer VALUES (013,'m','m',00113,12513);
INSERT INTO customer VALUES (014,'n','n',00114,12514);
INSERT INTO customer VALUES (015,'o','o',00115,12515);
INSERT INTO customer VALUES (016,'p','p',00116,12516);
INSERT INTO customer VALUES (017,'q','q',00117,12517);

INSERT INTO loan VALUES (001,251,3,002,12);
INSERT INTO loan VALUES (003,251,5,001,12);
INSERT INTO loan VALUES (002,2251,1,004,12);
INSERT INTO loan VALUES (004,2251,6,007,12);
INSERT INTO loan VALUES (005,2551,3,006,12);
INSERT INTO loan VALUES (006,2151,3,012,12);
INSERT INTO loan VALUES (007,34251,3,012,12);
INSERT INTO loan VALUES (008,456251,1,013,12);
INSERT INTO loan VALUES (009,1251,3,005,12);
INSERT INTO loan VALUES (010,251,1,008,12);
INSERT INTO loan VALUES (011,451251,3,0017,12);
INSERT INTO loan VALUES (012,1251,3,016,12);
INSERT INTO loan VALUES (013,251,3,014,12);
INSERT INTO loan VALUES (014,124251,1,011,12);
INSERT INTO loan VALUES (015,22451,3,012,12);
INSERT INTO loan VALUES (016,676251,3,002,12);
INSERT INTO loan VALUES (017,253421,9,008,12);
INSERT INTO loan VALUES (018,2521,3,009,12);
INSERT INTO loan VALUES (019,2151,5,001,12);
INSERT INTO loan VALUES (020,245651,3,003,12);
INSERT INTO loan VALUES (021,21451,7,007,12);
select * from loan;

SELECT * FROM loan ORDER BY amount DESC;

SELECT branch FROM loan;

select cust_id from customer natural join loan where amount>=5000 and amount <=15000;

select amount+(amount*intrest*0.01*1) as finalPay from customer natural join loan order by finalPay DESC LIMIT 1;
select cust_id,cust_name,(amount*intrest*0.01*1) as finalPay from customer natural join loan order by finalPay DESC LIMIT 1;


delimiter //
create procedure fun(in name varchar(20))
	begin
	select 
		select emp_name,salary from emp_details where emp_name=@name;
	end; //
