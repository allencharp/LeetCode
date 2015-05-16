delete from Person WHERE id not in
(
	select * from 
	(
		select * from 
		(
			select min(n.id)
			from Person n 
			group by n.email
		) a
	)x
)