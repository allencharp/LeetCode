CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE result int;  
  
  DECLARE sumcount int;
  SELECT COUNT(DISTINCT salary) INTO sumcount FROM Employee;
  
  IF(N > sumcount)
	THEN RETURN NULL;
  END IF;
  
  SELECT * INTO result FROM
	(
	SELECT Salary FROM Employee GROUP BY Salary ORDER BY Salary DESC LIMIT N
	) t
	ORDER BY t.Salary
	LIMIT 1;
	RETURN result;
END;