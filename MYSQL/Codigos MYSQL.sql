#-----------------------------------------------------------------------

SELECT COUNT(id) as total FROM wp_bp_free_users WHERE gender = '$gender'


#-----------------------------------------------------------------------
# Contar Duplicados
#-----------------------------------------------------------------------
SELECT
DISTINCT(capacitacion_id) as id,
COUNT(capacitacion_id ) as total
FROM capacitaciones_usuarios
GROUP BY capacitacion_id
HAVING total > 0

#-----------------------------------------------------------------------

SELECT 
c.id as id,
c.nombre as nombre,
c.fecha as fecha,
c.hora as hora,
c.cupos as total_cupos,
IF( cu_count.total IS NULL, c.cupos, c.cupos - cu_count.total ) as cupos,
IF( cu.id IS NULL,0,1) AS activo
FROM capacitaciones  c
LEFT JOIN capacitaciones_usuarios cu ON ( c.id = cu.capacitacion_id AND cu.usuario_id = 1 )
LEFT JOIN (
	SELECT
	DISTINCT(capacitacion_id) as id,
	COUNT(capacitacion_id ) as total
	FROM capacitaciones_usuarios
	GROUP BY capacitacion_id
) cu_count ON c.id = cu_count.id 

#-----------------------------------------------------------------------

SELECT id FROM {$prefix}bp_xprofile_fields AS x
WHERE x.name LIKE '%last%'


#-----------------------------------------------------------------------

SELECT  meta_key as name, meta_value as val
FROM {$wpdb->prefix}usermeta
WHERE user_id = $id
AND ( 
		meta_key = 'Youtube'
		OR meta_key = 'Facebook'
		OR meta_key = 'Instagram'
		OR meta_key = 'Twitter'
) ORDER BY name


#-----------------------------------------------------------------------

SELECT
	c.id as id,
	c.nombre as nombre,
	c.fecha as fecha,
	c.hora as hora,
	c.cupos - c.cupos_activos as cupos,
  	IF( cu.id IS NULL,0,1) AS activo
FROM capacitaciones c
left JOIN capacitaciones_usuarios cu ON ( c.id = cu.capacitacion_id AND cu.usuario_id = $id )

#-----------------------------------------------------------------------

SELECT u.user_id FROM {$prefix}pmpro_memberships_users AS u
INNER JOIN wp_pmpro_membership_levels l ON u.membership_id = l.id
WHERE u.status = 'active'
AND ( l.name LIKE '%premium%' OR l.name LIKE '%inactive%' OR l.name LIKE '%free%')

#-----------------------------------------------------------------------

SELECT id
FROM ( 

	# Final table with required fields id, name, username and email
	SELECT wpu.ID as id, wpu.user_login as username, wpu.user_email as email, bpu.name
	FROM users AS wpu
	INNER JOIN (

		# FIRST NAME table with LAST NAME table Left Joined to make the FULL NAME
		SELECT x.user_id AS id, CONCAT( x.value , ' ', COALESCE( res.value, '') ) AS name
		FROM bp_xprofile_data AS x 
		LEFT JOIN ( 		
			# LAST NAME table
			SELECT x.user_id, x.value
			FROM bp_xprofile_data AS x 
			WHERE x.field_id = $last_name_id
		) AS res
		ON x.user_id = res.user_id
		WHERE x.field_id = 1 

	) AS bpu
	ON wpu.ID = bpu.id

) AS f
WHERE name LIKE '%term%'
OR username LIKE '%term%'
OR email LIKE '%term%'


#-----------------------------------------------------------------------


SELECT d.field_id id, f.name name, d.value val
FROM bp_xprofile_data d
INNER JOIN bp_xprofile_fields f  ON d.field_id = f.id
WHERE d.user_id = $id 
AND (		
	f.name LIKE '%occupation%'
	OR f.name LIKE '%gender%'
	OR f.name LIKE '%ethnicity%'
	OR f.name LIKE '%age%' 
	OR f.name LIKE '%birthdate%' 
	OR f.name LIKE '%phone%' 
	OR f.name LIKE '%interest%' 
	OR f.name LIKE '%meeting%' 	
)
ORDER BY f.field_order ASC
