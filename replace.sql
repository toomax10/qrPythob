	
	
UPDATE tbm_solicitudes_2023 AS A
	SET A.sl_n_iniciativa = REPLACE( A.sl_n_iniciativa , "
", " " ) ;


UPDATE tbm_solicitudes_2025 AS A
	SET A.sl_asunto = REPLACE( A.sl_asunto, "
", " " ) ;

	