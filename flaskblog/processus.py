def noquality():

	data = [{"Cycle_time":59,"Maximum_injection_pressure":301,"Melt_temperature":196,"Mold_wall_temperature":150,"Packing_pressure":96,"Packing_time":2,"Part_weight":302,"Quality":0,"Sequence":31},
			{"Cycle_time":61,"Maximum_injection_pressure":298,"Melt_temperature":186,"Mold_wall_temperature":138,"Packing_pressure":96,"Packing_time":2,"Part_weight":299,"Quality":0,"Sequence":411},
			{"Cycle_time":61,"Maximum_injection_pressure":289,"Melt_temperature":217,"Mold_wall_temperature":148,"Packing_pressure":97,"Packing_time":2,"Part_weight":300,"Quality":0,"Sequence":495},
			{"Cycle_time":61,"Maximum_injection_pressure":307,"Melt_temperature":208,"Mold_wall_temperature":146,"Packing_pressure":113,"Packing_time":2,"Part_weight":291,"Quality":0,"Sequence":548},
			{"Cycle_time":62,"Maximum_injection_pressure":292,"Melt_temperature":200,"Mold_wall_temperature":148,"Packing_pressure":86,"Packing_time":2,"Part_weight":317,"Quality":0,"Sequence":555},
			{"Cycle_time":59,"Maximum_injection_pressure":303,"Melt_temperature":201,"Mold_wall_temperature":151,"Packing_pressure":103,"Packing_time":2,"Part_weight":282,"Quality":0,"Sequence":592},{"Cycle_time":60,"Maximum_injection_pressure":309,"Melt_temperature":210,"Mold_wall_temperature":143,"Packing_pressure":88,"Packing_time":2,"Part_weight":289,"Quality":0,"Sequence":670},
			{"Cycle_time":59,"Maximum_injection_pressure":306,"Melt_temperature":196,"Mold_wall_temperature":134,"Packing_pressure":109,"Packing_time":2,"Part_weight":306,"Quality":0,"Sequence":727},{"Cycle_time":61,"Maximum_injection_pressure":311,"Melt_temperature":201,"Mold_wall_temperature":163,"Packing_pressure":101,"Packing_time":2,"Part_weight":292,"Quality":0,"Sequence":923},
			{"Cycle_time":60,"Maximum_injection_pressure":292,"Melt_temperature":192,"Mold_wall_temperature":147,"Packing_pressure":104,"Packing_time":2,"Part_weight":307,"Quality":0,"Sequence":950},{"Cycle_time":60,"Maximum_injection_pressure":288,"Melt_temperature":190,"Mold_wall_temperature":154,"Packing_pressure":104,"Packing_time":2,"Part_weight":301,"Quality":0,"Sequence":1226},
			{"Cycle_time":60,"Maximum_injection_pressure":310,"Melt_temperature":209,"Mold_wall_temperature":154,"Packing_pressure":104,"Packing_time":2,"Part_weight":307,"Quality":0,"Sequence":1287},
			{"Cycle_time":61,"Maximum_injection_pressure":288,"Melt_temperature":205,"Mold_wall_temperature":160,"Packing_pressure":95,"Packing_time":2,"Part_weight":290,"Quality":0,"Sequence":1308},{"Cycle_time":61,"Maximum_injection_pressure":290,"Melt_temperature":193,"Mold_wall_temperature":163,"Packing_pressure":95,"Packing_time":2,"Part_weight":290,"Quality":0,"Sequence":1333},
			{"Cycle_time":62,"Maximum_injection_pressure":306,"Melt_temperature":196,"Mold_wall_temperature":152,"Packing_pressure":101,"Packing_time":2,"Part_weight":296,"Quality":0,"Sequence":1374},
			{"Cycle_time":61,"Maximum_injection_pressure":308,"Melt_temperature":183,"Mold_wall_temperature":146,"Packing_pressure":82,"Packing_time":2,"Part_weight":310,"Quality":0,"Sequence":1416},{"Cycle_time":60,"Maximum_injection_pressure":290,"Melt_temperature":217,"Mold_wall_temperature":154,"Packing_pressure":110,"Packing_time":2,"Part_weight":299,"Quality":0,"Sequence":1431},{"Cycle_time":60,"Maximum_injection_pressure":310,"Melt_temperature":213,"Mold_wall_temperature":165,"Packing_pressure":109,"Packing_time":2,"Part_weight":299,"Quality":0,"Sequence":1460},{"Cycle_time":61,"Maximum_injection_pressure":297,"Melt_temperature":202,"Mold_wall_temperature":146,"Packing_pressure":85,"Packing_time":2,"Part_weight":300,"Quality":0,"Sequence":1611},{"Cycle_time":60,"Maximum_injection_pressure":317,"Melt_temperature":195,"Mold_wall_temperature":156,"Packing_pressure":115,"Packing_time":2,"Part_weight":281,"Quality":0,"Sequence":1661},{"Cycle_time":60,"Maximum_injection_pressure":309,"Melt_temperature":214,"Mold_wall_temperature":141,"Packing_pressure":95,"Packing_time":2,"Part_weight":296,"Quality":0,"Sequence":1675},{"Cycle_time":60,"Maximum_injection_pressure":316,"Melt_temperature":214,"Mold_wall_temperature":155,"Packing_pressure":103,"Packing_time":2,"Part_weight":296,"Quality":0,"Sequence":2039},{"Cycle_time":59,"Maximum_injection_pressure":319,"Melt_temperature":202,"Mold_wall_temperature":157,"Packing_pressure":94,"Packing_time":2,"Part_weight":292,"Quality":0,"Sequence":2088},{"Cycle_time":60,"Maximum_injection_pressure":294,"Melt_temperature":190,"Mold_wall_temperature":150,"Packing_pressure":104,"Packing_time":2,"Part_weight":302,"Quality":0,"Sequence":2227},{"Cycle_time":61,"Maximum_injection_pressure":299,"Melt_temperature":207,"Mold_wall_temperature":162,"Packing_pressure":94,"Packing_time":2,"Part_weight":295,"Quality":0,"Sequence":2244},
			{"Cycle_time":60,"Maximum_injection_pressure":295,"Melt_temperature":212,"Mold_wall_temperature":158,"Packing_pressure":100,"Packing_time":2,"Part_weight":291,"Quality":0,"Sequence":2397},{"Cycle_time":61,"Maximum_injection_pressure":280,"Melt_temperature":194,"Mold_wall_temperature":146,"Packing_pressure":88,"Packing_time":2,"Part_weight":305,"Quality":0,"Sequence":2408},
			{"Cycle_time":61,"Maximum_injection_pressure":286,"Melt_temperature":198,"Mold_wall_temperature":136,"Packing_pressure":104,"Packing_time":2,"Part_weight":310,"Quality":0,"Sequence":2449},{"Cycle_time":61,"Maximum_injection_pressure":292,"Melt_temperature":209,"Mold_wall_temperature":139,"Packing_pressure":87,"Packing_time":2,"Part_weight":291,"Quality":0,"Sequence":2459},{"Cycle_time":60,"Maximum_injection_pressure":300,"Melt_temperature":208,"Mold_wall_temperature":147,"Packing_pressure":105,"Packing_time":2,"Part_weight":301,"Quality":0,"Sequence":2738},{"Cycle_time":60,"Maximum_injection_pressure":315,"Melt_temperature":186,"Mold_wall_temperature":151,"Packing_pressure":102,"Packing_time":2,"Part_weight":307,"Quality":0,"Sequence":2801},{"Cycle_time":60,"Maximum_injection_pressure":299,"Melt_temperature":198,"Mold_wall_temperature":161,"Packing_pressure":96,"Packing_time":2,"Part_weight":306,"Quality":0,"Sequence":2875},{"Cycle_time":61,"Maximum_injection_pressure":319,"Melt_temperature":195,"Mold_wall_temperature":148,"Packing_pressure":96,"Packing_time":2,"Part_weight":297,"Quality":0,"Sequence":3032},{"Cycle_time":60,"Maximum_injection_pressure":300,"Melt_temperature":215,"Mold_wall_temperature":142,"Packing_pressure":113,"Packing_time":2,"Part_weight":292,"Quality":0,"Sequence":3099},{"Cycle_time":60,"Maximum_injection_pressure":302,"Melt_temperature":204,"Mold_wall_temperature":135,"Packing_pressure":90,"Packing_time":2,"Part_weight":294,"Quality":0,"Sequence":3174},{"Cycle_time":59,"Maximum_injection_pressure":282,"Melt_temperature":188,"Mold_wall_temperature":157,"Packing_pressure":109,"Packing_time":2,"Part_weight":311,"Quality":0,"Sequence":3272},{"Cycle_time":60,"Maximum_injection_pressure":301,"Melt_temperature":200,"Mold_wall_temperature":153,"Packing_pressure":96,"Packing_time":2,"Part_weight":307,"Quality":0,"Sequence":3275},{"Cycle_time":60,"Maximum_injection_pressure":302,"Melt_temperature":205,"Mold_wall_temperature":158,"Packing_pressure":109,"Packing_time":2,"Part_weight":313,"Quality":0,"Sequence":3364},{"Cycle_time":60,"Maximum_injection_pressure":288,"Melt_temperature":206,"Mold_wall_temperature":147,"Packing_pressure":88,"Packing_time":2,"Part_weight":281,"Quality":0,"Sequence":3423},{"Cycle_time":61,"Maximum_injection_pressure":294,"Melt_temperature":204,"Mold_wall_temperature":154,"Packing_pressure":104,"Packing_time":2,"Part_weight":310,"Quality":0,"Sequence":3598},{"Cycle_time":59,"Maximum_injection_pressure":291,"Melt_temperature":190,"Mold_wall_temperature":152,"Packing_pressure":87,"Packing_time":2,"Part_weight":296,"Quality":0,"Sequence":3691},{"Cycle_time":59,"Maximum_injection_pressure":289,"Melt_temperature":185,"Mold_wall_temperature":160,"Packing_pressure":113,"Packing_time":2,"Part_weight":306,"Quality":0,"Sequence":3980},{"Cycle_time":59,"Maximum_injection_pressure":296,"Melt_temperature":192,"Mold_wall_temperature":150,"Packing_pressure":88,"Packing_time":2,"Part_weight":298,"Quality":0,"Sequence":4032},{"Cycle_time":61,"Maximum_injection_pressure":306,"Melt_temperature":208,"Mold_wall_temperature":159,"Packing_pressure":81,"Packing_time":2,"Part_weight":310,"Quality":0,"Sequence":4142},{"Cycle_time":61,"Maximum_injection_pressure":294,"Melt_temperature":207,"Mold_wall_temperature":161,"Packing_pressure":94,"Packing_time":2,"Part_weight":304,"Quality":0,"Sequence":4294},{"Cycle_time":60,"Maximum_injection_pressure":303,"Melt_temperature":210,"Mold_wall_temperature":140,"Packing_pressure":106,"Packing_time":2,"Part_weight":285,"Quality":0,"Sequence":4393},{"Cycle_time":60,"Maximum_injection_pressure":306,"Melt_temperature":201,"Mold_wall_temperature":148,"Packing_pressure":90,"Packing_time":2,"Part_weight":299,"Quality":0,"Sequence":4614},{"Cycle_time":59,"Maximum_injection_pressure":290,"Melt_temperature":200,"Mold_wall_temperature":149,"Packing_pressure":104,"Packing_time":2,"Part_weight":315,"Quality":0,"Sequence":4721},{"Cycle_time":60,"Maximum_injection_pressure":306,"Melt_temperature":214,"Mold_wall_temperature":140,"Packing_pressure":102,"Packing_time":2,"Part_weight":289,"Quality":0,"Sequence":4836},{"Cycle_time":58,"Maximum_injection_pressure":303,"Melt_temperature":196,"Mold_wall_temperature":152,"Packing_pressure":98,"Packing_time":2,"Part_weight":293,"Quality":0,"Sequence":4891},{"Cycle_time":60,"Maximum_injection_pressure":312,"Melt_temperature":215,"Mold_wall_temperature":158,"Packing_pressure":81,"Packing_time":2,"Part_weight":290,"Quality":0,"Sequence":4929},{"Cycle_time":60,"Maximum_injection_pressure":300,"Melt_temperature":189,"Mold_wall_temperature":152,"Packing_pressure":100,"Packing_time":2,"Part_weight":302,"Quality":0,"Sequence":5201},{"Cycle_time":58,"Maximum_injection_pressure":303,"Melt_temperature":197,"Mold_wall_temperature":151,"Packing_pressure":113,"Packing_time":2,"Part_weight":317,"Quality":0,"Sequence":5314},{"Cycle_time":60,"Maximum_injection_pressure":306,"Melt_temperature":195,"Mold_wall_temperature":160,"Packing_pressure":100,"Packing_time":2,"Part_weight":298,"Quality":0,"Sequence":5512},{"Cycle_time":61,"Maximum_injection_pressure":291,"Melt_temperature":199,"Mold_wall_temperature":157,"Packing_pressure":100,"Packing_time":2,"Part_weight":309,"Quality":0,"Sequence":5614},{"Cycle_time":60,"Maximum_injection_pressure":298,"Melt_temperature":203,"Mold_wall_temperature":143,"Packing_pressure":115,"Packing_time":2,"Part_weight":318,"Quality":0,"Sequence":5749},{"Cycle_time":59,"Maximum_injection_pressure":295,"Melt_temperature":204,"Mold_wall_temperature":157,"Packing_pressure":117,"Packing_time":2,"Part_weight":315,"Quality":0,"Sequence":5852},{"Cycle_time":61,"Maximum_injection_pressure":294,"Melt_temperature":194,"Mold_wall_temperature":153,"Packing_pressure":90,"Packing_time":2,"Part_weight":308,"Quality":0,"Sequence":5956},{"Cycle_time":59,"Maximum_injection_pressure":283,"Melt_temperature":200,"Mold_wall_temperature":160,"Packing_pressure":108,"Packing_time":2,"Part_weight":289,"Quality":0,"Sequence":6387},{"Cycle_time":58,"Maximum_injection_pressure":303,"Melt_temperature":204,"Mold_wall_temperature":156,"Packing_pressure":90,"Packing_time":2,"Part_weight":299,"Quality":0,"Sequence":6499},{"Cycle_time":60,"Maximum_injection_pressure":315,"Melt_temperature":196,"Mold_wall_temperature":167,"Packing_pressure":101,"Packing_time":2,"Part_weight":307,"Quality":0,"Sequence":6554},{"Cycle_time":61,"Maximum_injection_pressure":285,"Melt_temperature":184,"Mold_wall_temperature":148,"Packing_pressure":104,"Packing_time":2,"Part_weight":283,"Quality":0,"Sequence":6821},{"Cycle_time":59,"Maximum_injection_pressure":293,"Melt_temperature":199,"Mold_wall_temperature":149,"Packing_pressure":110,"Packing_time":2,"Part_weight":303,"Quality":0,"Sequence":6850},{"Cycle_time":60,"Maximum_injection_pressure":296,"Melt_temperature":200,"Mold_wall_temperature":167,"Packing_pressure":89,"Packing_time":2,"Part_weight":293,"Quality":0,"Sequence":7103},{"Cycle_time":60,"Maximum_injection_pressure":305,"Melt_temperature":204,"Mold_wall_temperature":144,"Packing_pressure":95,"Packing_time":2,"Part_weight":308,"Quality":0,"Sequence":7271},{"Cycle_time":59,"Maximum_injection_pressure":291,"Melt_temperature":187,"Mold_wall_temperature":144,"Packing_pressure":95,"Packing_time":2,"Part_weight":302,"Quality":0,"Sequence":7423},{"Cycle_time":59,"Maximum_injection_pressure":299,"Melt_temperature":206,"Mold_wall_temperature":154,"Packing_pressure":110,"Packing_time":2,"Part_weight":287,"Quality":0,"Sequence":7438},{"Cycle_time":61,"Maximum_injection_pressure":290,"Melt_temperature":217,"Mold_wall_temperature":156,"Packing_pressure":97,"Packing_time":2,"Part_weight":295,"Quality":0,"Sequence":7677},{"Cycle_time":61,"Maximum_injection_pressure":313,"Melt_temperature":200,"Mold_wall_temperature":159,"Packing_pressure":89,"Packing_time":2,"Part_weight":301,"Quality":0,"Sequence":7942},{"Cycle_time":61,"Maximum_injection_pressure":300,"Melt_temperature":192,"Mold_wall_temperature":150,"Packing_pressure":90,"Packing_time":2,"Part_weight":319,"Quality":0,"Sequence":8322},{"Cycle_time":61,"Maximum_injection_pressure":314,"Melt_temperature":206,"Mold_wall_temperature":148,"Packing_pressure":100,"Packing_time":2,"Part_weight":298,"Quality":0,"Sequence":8823},{"Cycle_time":61,"Maximum_injection_pressure":298,"Melt_temperature":205,"Mold_wall_temperature":148,"Packing_pressure":108,"Packing_time":2,"Part_weight":316,"Quality":0,"Sequence":8884},{"Cycle_time":60,"Maximum_injection_pressure":285,"Melt_temperature":194,"Mold_wall_temperature":154,"Packing_pressure":106,"Packing_time":2,"Part_weight":288,"Quality":0,"Sequence":8946},{"Cycle_time":59,"Maximum_injection_pressure":294,"Melt_temperature":215,"Mold_wall_temperature":152,"Packing_pressure":100,"Packing_time":2,"Part_weight":300,"Quality":0,"Sequence":8996},{"Cycle_time":60,"Maximum_injection_pressure":300,"Melt_temperature":219,"Mold_wall_temperature":158,"Packing_pressure":114,"Packing_time":2,"Part_weight":303,"Quality":0,"Sequence":9021},{"Cycle_time":60,"Maximum_injection_pressure":301,"Melt_temperature":193,"Mold_wall_temperature":149,"Packing_pressure":97,"Packing_time":2,"Part_weight":298,"Quality":0,"Sequence":9611},{"Cycle_time":59,"Maximum_injection_pressure":298,"Melt_temperature":185,"Mold_wall_temperature":142,"Packing_pressure":83,"Packing_time":2,"Part_weight":300,"Quality":0,"Sequence":9644},
			{"Cycle_time":60,"Maximum_injection_pressure":301,"Melt_temperature":204,"Mold_wall_temperature":155,"Packing_pressure":100,"Packing_time":2,"Part_weight":291,"Quality":0,"Sequence":9692},{"Cycle_time":61,"Maximum_injection_pressure":294,"Melt_temperature":219,"Mold_wall_temperature":153,"Packing_pressure":99,"Packing_time":2,"Part_weight":303,"Quality":0,"Sequence":9705}]

	return data