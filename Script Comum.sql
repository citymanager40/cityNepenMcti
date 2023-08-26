-- ################
-- #    SCHEMA    #
-- ################

CREATE SCHEMA comum;

-- ################
-- #  SEQUENCES   #
-- ################

CREATE SEQUENCE comum.usuario_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

  -- ################
-- #    TABLES    #
-- ################

CREATE TABLE comum.tb_usuario_usu (
	id_usuario_usu integer NOT NULL DEFAULT nextval('comum.usuario_seq'::regclass),
	txt_nome_usu varchar(200) NOT NULL,
	txt_email_usu varchar(200) NOT NULL,
  txt_cpf_usu varchar(11) NOT NULL,
	CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario_usu)
);

-- ####################################
-- #        INSERTS PARA TESTES       #
-- ####################################

INSERT INTO comum.tb_usuario_usu(txt_nome_usu, txt_email_usu, txt_cpf_usu) VALUES('Admin', 'admin@urbanmob.com.br', '11111111111');

INSERT INTO comum.tb_usuario_usu(txt_nome_usu, txt_email_usu, txt_cpf_usu) VALUES('Governo', 'governo@urbanmob.com.br', '22222222222');
INSERT INTO comum.tb_usuario_usu(txt_nome_usu, txt_email_usu, txt_cpf_usu) VALUES('Usuário', 'user@urbanmob.com.br', '33333333333');
INSERT INTO comum.tb_usuario_usu(txt_nome_usu, txt_email_usu, txt_cpf_usu) VALUES('Usuário', 'user@urbanzone.com.br', '44444444444');
INSERT INTO comum.tb_usuario_usu(txt_nome_usu, txt_email_usu, txt_cpf_usu) VALUES('Usuário', 'user@urbanpass.com.br', '55555555555');
INSERT INTO comum.tb_usuario_usu(txt_nome_usu, txt_email_usu, txt_cpf_usu) VALUES('Governo', 'governo@urbanpass.com.br', '66666666666');