const data = [
	{
		name: "Home",
		products: []
	},

	{
		name: "Drinks",
		menu: [
			{
				name: "Cerveza",
				products: [
					{
						url:
							"https://www.tiendainglesa.com.uy/Cerveza_PATAGONIA_IPA_24.7_lata_473ml.producto?355674",
						price: "109",
						name: "PATAGONIA IPA 24.7 lata 473ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Cerveza_STELLA_ARTOIS_botella_975ml.producto?11961",
						price: "148",
						name: "STELLA ARTOIS botella 975ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Cerveza_PATAGONIA_Amber_Lager_740ml.producto?322158",
						price: "183",
						name: "PATAGONIA Amber Lager 740ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Cerveza_BRAHMA_Chopp_473ml.producto?280054",
						price: "57",
						name: "BRAHMA Chopp 473ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Cerveza_ZILLERTAL_botella_970cc.producto?6366",
						price: "127",
						name: "ZILLERTAL botella 970cc"
					},

					{
						url:
							"https://www.tiendainglesa.com.uy/Cerveza_PILSEN_Soul_sin_Alcohol_960cc.producto?283492",
						price: "94",
						name: "PILSEN Soul sin Alcohol 960cc"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Cerveza_STELLA_ARTOIS_lata_473ml.producto?338550",
						price: "87",
						name: "STELLA ARTOIS lata 473ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Cerveza_CORONA_botella_710ml.producto?12586",
						price: "140",
						name: "CORONA botella 710ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Cerveza_HEINEKEN_botella_descartable_1l.producto?279660",
						price: "150",
						name: "HEINEKEN botella descartable 1l"
					}
				]
			},
			{
				name: "Vino",
				products: [
					{
						url:
							"https://www.tiendainglesa.com.uy/Vino_Tinto_Concha_y_Toro_Carmenere_Reservado_750ml.producto?9233",
						price: "235",
						name: "Tinto Concha y Toro Carmenere Reservado 750ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Vino_Blanco_Don_Pascual_Brut_Blanc_de_Blancs_750cc.producto?6257",
						price: "195",
						name: "Blanco Don Pascual Brut Blanc de Blancs 750cc"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Vino_Tinto_CONCHA_Y_TORO_Cabernet_Sauvignon_Reservado_750ml.producto?5871",
						price: "229",
						name: "Tinto CONCHA Y TORO Cabernet Sauvignon Reservado 750ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Vino_Tinto_H._STAGNARI_Premier_Tannat_750ml.producto?2371",
						price: "279",
						name: "Tinto H. STAGNARI Premier Tannat 750ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Vino_Tinto_Concha_y_Toro_Reservado_Malbec_750ml.producto?294690",
						price: "235",
						name: "Tinto Concha y Toro Reservado Malbec 750ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Vino_Tinto_TRAPICHE_Malbec_750ml.producto?6813",
						price: "235",
						name: "Tinto TRAPICHE Malbec 750ml"
					},

					{
						url:
							"https://www.tiendainglesa.com.uy/Vino_Tinto_Benjamin_NIETO_SENETINER_Malbec_750cc.producto?9011",
						price: "209",
						name: "Tinto Benjamin NIETO SENETINER Malbec 750cc"
					},

					{
						url:
							"https://www.tiendainglesa.com.uy/Vino_Tinto_Don_Pascual_Tannat_750ml.producto?5767",
						price: "195",
						name: "Tinto Don Pascual Tannat 750ml"
					}
				]
			},

			{
				name: "Refresco",
				products: [
					{
						url:
							"https://www.tiendainglesa.com.uy/Refresco_Coca_Cola_Light_600ml.producto?8525",
						price: "47",
						name: "Coca Cola Light 600ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Refresco_Sprite_Zero_1%2C5l.producto?8502",
						price: "96",
						name: "Sprite Zero 1,5l"
					},

					{
						url:
							"https://www.tiendainglesa.com.uy/Refresco_COCA_COLA_Light_descartable_1.5l.producto?2545",
						price: "105",
						name: "COCA COLA Light descartable 1.5l"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Refresco_Schweppes_Zero_sabor_Pomelo_1%2C5l.producto?319190",
						price: "89",
						name: "Schweppes Zero sabor Pomelo 1,5l"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Refresco_Pomelo_Light_Paso_de_los_Toros_1%2C5l.producto?6989",
						price: "95",
						name: "Pomelo Light Paso de los Toros 1,5l"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Refresco_Coca_Cola_600ml.producto?8524",
						price: "47",
						name: "Coca Cola 600ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Refresco_Coca_Cola_Light_250ml.producto?311806",
						price: "22",
						name: "Coca Cola Light 250ml"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Refresco_Sprite_Zero_600ml.producto?8503",
						price: "47",
						name: "Sprite Zero 600ml"
					}
				]
			},
			{
				name: "Whisky",
				products: [
					{
						url:
							"https://www.tiendainglesa.com.uy/Whisky_Johnnie_Walker_Black_Label_1l.producto?710",
						price: "150",
						name: "Johnnie Walker Black Label"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Whisky_Johnnie_Walker_Double_Black_1l.producto?217438",
						price: "200",
						name: "Johnnie Walker Double Black 1l"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Whisky_Johnnie_Walker_Red_Label_1l.producto?23616",
						price: "150",
						name: "Johnnie Walker Red Label "
					},

					{
						url:
							"https://www.tiendainglesa.com.uy/Whisky_Ye_Monks_1l.producto?8353",
						price: "120",
						name: "Ye Monks"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Whisky_100_Pipers_1l_%2B_Petaca_200ml.producto?297814",
						price: "419",
						name: "100 Pipers"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Whisky_Sandy_Mac_1l.producto?6825",
						price: "120",
						name: "Sandy Mac"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Whisky_Something_Special_1l.producto?1301",
						price: "100",
						name: "Something Special"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Whisky_Sandy_Mac_1l_%2B_Petaca_200ml.producto?242373",
						price: "120",
						name: "Sandy Mac"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Whisky_Vat_69_1l.producto?6051",
						price: "90",
						name: "Vat 69"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Whisky_Sir_Edwards_1l.producto?7145",
						price: "429",
						name: "Sir Edwards"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Whisky_White_Horse_1l.producto?1025",
						price: "120",
						name: "White Horse"
					},
					{
						url:
							"https://www.tiendainglesa.com.uy/Whisky_100_Pipers_1l.producto?1411",
						price: "459",
						name: "100 Pipers"
					}
				]
			}
		]
	},
	{
		name: "Food",
		menu: [
			{
				name: "Main Dishes",
				products: [
					{
						
						price: "350",
						name:
							"Sopa de Mariscos, pescado, camarón, cangrejo, calamar y pulpo en un consomé de vino blanco y ajo."
					},
					{
						price: "350",
						name: "Pescado Entero frito con arroz y vegetales"
					},
					{
						
						price: "350",
						name:
							"Filete de Pescado, empanizado o a la plancha con arroz y vegetales"
					},
					{
						
						price: "350",
						name:
							"Atún a la Plancha, filete de atun servido con pasta japonesa, vegetales y wasabi"
					},
					{
						
						price: "350",
						name: "Arroz con Pollo con ensalada mixta o papas fritas!"
					},
					{
						
						price: "350",
						name: "Arroz con Camarones con encalada mixta o papas fritas"
					},
					{
						
						price: "350",
						name: "Arroz con Mariscos con ensalada mixta o papas fritas!"
					},
					{
						
						price: "350",
						name:
							"Camarones Jumbo, al gusto empanizados a la plancha o al ajillo, acompañado de ensalada y pure de papa"
					},
					{
						
						price: "350",
						name:
							"Pollo a la Parmesana, empanizado con salsa marinara casera y queso mozzarella, servido con un acompañamiento de espaghetti marinara y vegetales."
					},
					{
						
						price: "350",
						name:
							"Linguini con Camarones, pasta con camarones, Salsa de soya, ajonjolí y especies."
					},
					{
						
						price: "350",
						name:
							"Espaguetti de la Casa, salsa de tomate casera con ajo aceite de oliva y albahaca fresca con pan de ajo"
					}
				]
			},
			{

			name: "Entrances",

				products: [
					{
						name: "Risotto",
						price: 320
					},
					{
						name: "Lasaña",
						price: 230
					},
					{
						name: "Polenta",
						price: 230
					},
					{
						name: "Pizza",
						price: 200
					}
				]
			},
			{

			name: "Desserts",
				products: [
					{
						name: "German chocolate cake",
						price: 420
					},
					{
						name: "Angel cake",
						price: 430
					},
					{
						name: "Blondie",
						price: 430
					},
					{
						name: "Cassata",
						price: 420
					},
					{
						name: "German chocolate cake",
						price: 420
					},
					{
						name: "Angel cake",
						price: 430
					},
					{
						name: "Blondie",
						price: 430
					},
					{
						name: "Cassata",
						price: 420
					}
				]
			}
		]
	},

	{
		name: "Services",
		products: [
			{
				name: "Personal Cheaf",
				menu: []
			},
			{
				name: "Parties",
				menu: []
			},
			{ name: "Barman", menu: [] }
		]
	}
	//   ,
	//   {
	// 		name: "Contact",
	// 		menu: [{ name: "Contact", menu: [] }, { name: "Our story", menu: [] }]
	// 	}
];


