
# Para evitar conflictos al borrar tablas con llaves foraneas
SET FOREIGN_KEY_CHECKS = 0;
	 
# ----------------------------------------------------------------
# Tabla login_attempts - Tabla interna para el sistema de logueo
# ----------------------------------------------------------------

DROP TABLE IF EXISTS `login_attempts`;

CREATE TABLE `login_attempts` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `ip_address` varchar(45) NOT NULL,
  `login` varchar(100) NOT NULL,
  `time` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


# ----------------------------------------------------------------
# Tabla groups - Aqui guardamos los roles en caso de haber mas de dos
# ----------------------------------------------------------------

DROP TABLE IF EXISTS `groups`;

CREATE TABLE `groups` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `groups` (`id`, `name`, `description`) VALUES
     (1,'admin','Administrator'),
     (2,'members','General User');

	
# ----------------------------------------------------------------
# Tabla users - Aqui guardamos los usuarios
# ----------------------------------------------------------------

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `ip_address` varchar(45) NOT NULL,
  `username` varchar(100) NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `activation_selector` varchar(255) DEFAULT NULL,
  `activation_code` varchar(255) DEFAULT NULL,
  `forgotten_password_selector` varchar(255) DEFAULT NULL,
  `forgotten_password_code` varchar(255) DEFAULT NULL,
  `forgotten_password_time` int(11) unsigned DEFAULT NULL,
  `remember_selector` varchar(255) DEFAULT NULL,
  `remember_code` varchar(255) DEFAULT NULL,
  `created_on` int(11) unsigned NOT NULL,
  `last_login` int(11) unsigned DEFAULT NULL,
  `active` tinyint(1) unsigned DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `company` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `uc_email` UNIQUE (`email`),
  CONSTRAINT `uc_activation_selector` UNIQUE (`activation_selector`),
  CONSTRAINT `uc_forgotten_password_selector` UNIQUE (`forgotten_password_selector`),
  CONSTRAINT `uc_remember_selector` UNIQUE (`remember_selector`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `users` (`id`, `ip_address`, `username`, `password`, `email`, `activation_code`, `forgotten_password_code`, `created_on`, `last_login`, `active`, `first_name`, `last_name`, `company`, `phone`) VALUES
     ('1','127.0.0.1','administrator','$2y$08$0axElZRDtkpO5qcjDs3CeOFkp5Umx8RKsg5YwDm77ub97lS9CGBjm','admin@admin.com','',NULL,'1268889823','1268889823','1', 'Admin','istrator','ADMIN','0');

	 
# ----------------------------------------------------------------
# Tabla users_groups - Aqui guardamos los roles que le corresponden a un usuario
# ----------------------------------------------------------------

DROP TABLE IF EXISTS `users_groups`;

CREATE TABLE `users_groups` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `group_id` mediumint(8) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_users_groups_users1_idx` (`user_id`),
  KEY `fk_users_groups_groups1_idx` (`group_id`),
  CONSTRAINT `uc_users_groups` UNIQUE (`user_id`, `group_id`),
  CONSTRAINT `fk_users_groups_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_groups_groups1` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `users_groups` (`id`, `user_id`, `group_id`) VALUES
     (1,1,1),
     (2,1,2);

	 
	 
	 

# ----------------------------------------------------------------
# 		SISTEMA CAPACITACIONES
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# Tabla capacitaciones - Aqui guardamos las capacitaciones creadas
# ----------------------------------------------------------------

DROP TABLE IF EXISTS `capacitaciones`;

CREATE TABLE `capacitaciones` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `fecha` date NOT NULL,
  `hora` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# ----------------------------------------------------------------
# Tabla capacitaciones_stock - Aqui guardamos los cupos
# ----------------------------------------------------------------

DROP TABLE IF EXISTS `capacitaciones_stock`;

CREATE TABLE `capacitaciones_stock` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `capacitacion_id` INT(11) UNSIGNED NOT NULL,
  `cupos` INT(11) UNSIGNED NOT NULL,  
  PRIMARY KEY (`id`),
  KEY `fk_capacitaciones_stock_idx` (`capacitacion_id`),
  CONSTRAINT `uc_capacitacion_stock_capacitacion_id` UNIQUE (`capacitacion_id`),
  CONSTRAINT `fk_capacitacion_stock_capacitacion_id` FOREIGN KEY (`capacitacion_id`) REFERENCES `capacitaciones` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=INNODB DEFAULT CHARSET=utf8;


# ----------------------------------------------------------------
# Tabla capacitaciones - Aqui guardamos las relaciones entre capacitaciones y usuarios
# ----------------------------------------------------------------

DROP TABLE IF EXISTS `capacitaciones_usuarios`;

CREATE TABLE `capacitaciones_usuarios` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `usuario_id` INT(11) UNSIGNED NOT NULL,  
  `capacitacion_id` INT(11) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_capacitacion_idx` (`capacitacion_id`),
  KEY `fk_usuario_idx` (`usuario_id`),
  CONSTRAINT `uc_capacitaciones_usuarios_id` UNIQUE (`capacitacion_id`,`usuario_id`),
  CONSTRAINT `fk_capacitaciones_usuarios_capacitacion_id` FOREIGN KEY (`capacitacion_id`) REFERENCES `capacitaciones` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_capacitaciones_usuarios_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=INNODB DEFAULT CHARSET=utf8;


SET FOREIGN_KEY_CHECKS = 1;