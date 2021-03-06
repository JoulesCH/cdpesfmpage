import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import colors
 

def convocatoria():
   
    return [html.Div([
                                        html.H1("Convocatoria 2021-2", className="display-3" , style ={"font-size":"3rem"} ),
                                        html.P(
                                            "Falta muy poco para que puedas ser parte de nuestra comunidad",
                                            className="lead",
                                        ),
                                        html.P(
                                            "La convocatoria se abrirá la primera semana de regreso a clases (febrero 25-28), dando a conocer horarios, disponibilidad y fechas de inicio. ",
                                        ),
                                        html.P([
                                            "Requisitos indispensables: ",
                                            html.Ul([
                                                html.Li("Ser parte de la comunidad de estudiantes politécnica"),
                                                html.Li("Tener tu boleta y correo institucional activos"),
                                                html.Li("Si ya has tomado cursos en el CdP ESFM, tener tu ID de registro anterior")
                                            ])

                                        ])
                                        
                                        
                                                
                                                
                                            
                                        
                                        
                                        #html.P(html.A(dbc.Button("Unéte a Discord", color="primary"), href = "https://discord.gg/JxS59BFBu3",target="_blank" ), className="lead"),
                                    ], style = {"padding":"20px", "padding-top":20, "padding-bottom":5}),
                                    
                                    
        ]
def convocatoria2(ide = None, nombre = None, boleta = None, correo = None, carrera = None, semestre = None):
    margen = 25
    color_letra = '#000'#'#061d47'
    color_footer = '#8f8f8f'
    color_fondo = '#ffffff'
    width_input = 300
    #print(ide, "****")
    if not ide:
            return [html.Div([
                                            html.H1("Convocatoria 2021-2", className="display-3" , style ={"font-size":"3rem", "color":color_letra}, ),
                                            html.P(
                                                "Llena el siguiente formulario y espera una confirmación por e-mail",style = {"color":color_letra},
                                                className="lead",
                                            ),
                                        # html.Div(
                                        #         children = [
                                        #             html.Img (src="https://fotos.subefotos.com/b8055f292fdcc96840cc8cc172f6ab94o.png", 
                                        #                 style = {"margin-bottom":0,'min-width':450,"display":"block","width": '70%', "height": "auto", "margin-left": "auto", "margin-right": "auto", "margin-top": 30,"text-align":"center"})
                                        #         ] 
                                        #     ),
                                            dbc.Row([
                                                dbc.Col(html.Img (src='https://fotos.subefotos.com/dee1790fc6bec5718d06ec4c8d80ee71o.png', style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6),
                                                dbc.Col(html.Img (src='https://fotos.subefotos.com/673fd6a8b257776bc02619ac941b0783o.png', style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6),
                                                dbc.Col(html.Img (src='https://fotos.subefotos.com/8ad0901fd4fa9dbb648e720c3520b701o.png', style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6),
                                                dbc.Col(html.Img (src='https://fotos.subefotos.com/2eb394d174d94e6c0aff2a8f15cd7d42o.png', style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6),
                                                dbc.Col(html.Img (src='https://fotos.subefotos.com/a91e42ffd6b2dd249ecb4df0bb1c234do.png', style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6),
                                                dbc.Col(html.Img (src='https://fotos.subefotos.com/48b519d4b7109cb58d21dfceb259d54bo.png', style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6),
                                                #dbc.Col(html.Img (src='https://fotos.subefotos.com/dee1790fc6bec5718d06ec4c8d80ee71o.png'))
                                            ], justify = 'center'),
                                            html.Div(
                                            children =[ 
                                                    html.H6('Ingresa tu ID anterior  ', style = {'margin-top':margen,'color':color_letra}),
                                                        #dcc.Input(id = 'name',value='', type='text', style ={'width':'auto','width': 300}, placeholder = 'Empieza por tus nombres'),
                                                    html.Div([
                                                            dbc.Row([
                                                            dbc.Col([
                                                                dbc.Input(id = 'id_anterior',value='', type='text', style ={'width':'100%', 'margin-left':'auto','margin-right':'auto'}, placeholder = 'Puedes encontarlo en tu correo'),
                                                            ], width = 10),
                                                            dbc.Col([
                                                                dbc.Button('Ir', id = "id_boton")
                                                            ], width = 2)
                                                        ], no_gutters=True,),
                                                    ], style = {'width':300, 'margin-left':'auto','margin-right':'auto'}),
                                                    html.Div(id = 'mensaje-id'),
                                                        html.P('Si no has tomado cursos anteriores, ignóralo.', style = {'color':color_footer,'margin-top':10}),
                                                dbc.Row([
                                                    dbc.Col([
                                                        #html.Div('Horarios sujetos a cupo, si se excede el primer horario mostrado se abrirá el otro.', style = {'font-size':'0.7em','color':color_letra}),
                                                        html.H6('Ingresa tu nombre completo: ', style = {'margin-top':margen,'color':color_letra}),
                                                        #dcc.Input(id = 'name',value='', type='text', style ={'width':'auto','width': 300}, placeholder = 'Empieza por tus nombres'),
                                                        dbc.Input(id = 'name',value='', type='text', style ={'width':width_input, 'margin-left':'auto','margin-right':'auto'}, placeholder = 'Empieza por tus nombres'),
                                                        
                                                        html.H6('Ingresa tu número de boleta: ', style = {'margin-top':margen,'color':color_letra}),
                                                        #dcc.Input(id = 'boleta',value='', type='number', style ={'width':'auto','width': 300}),
                                                        dbc.Input(id = 'boleta',value='', type='number', style ={'width': width_input, 'margin-left':'auto','margin-right':'auto'}),

                                                        html.H6('Ingresa tu correo institucional: ', style = {'margin-top':margen,'color':color_letra}),
                                                        #dcc.Input(id = 'correo',value='', type='email', style ={'width':'auto','width': 300}, placeholder = 'nombre@alumno.ipn.mx'),
                                                        dbc.Input(id = 'correo',value='', type='email', style ={'width': width_input, 'margin-left':'auto','margin-right':'auto'}, placeholder = 'nombre@alumno.ipn.mx'),
                                                        html.P('Si aún no tienes correo institucional ingresa otro correo.', style = {'color':color_footer,'margin-top':10}),
                                                    ], lg = 4),
                                                    dbc.Col([
                                                        html.H6('Elige tu carrera:', style = {'margin-top':margen,'color':color_letra}),

                                                        dcc.Dropdown(id = 'carrera',
                                                            options=[
                                                                {'label': 'Lic. en Matemática Algorítmica', 'value': 'Mat'},
                                                                {'label': 'Lic. en Física y Matemáticas', 'value': 'Lic'},
                                                                {'label': 'Ingeniería Matemática', 'value': 'Ing'},
                                                            
                                                            ],
                                                            value='',
                                                            multi = False, 
                                                            searchable = False,
                                                            clearable = False,
                                                            style = {
                                                                'width': width_input,
                                                                'margin-left':'auto',
                                                                'margin-right':'auto'
                                                            }, placeholder = 'Carreras'
                                                        ),
                                                        html.H6('Elige tu semestre:', style = {'margin-top':margen,'color':color_letra}),
                                                        html.Div( children = [
                                                                                dcc.Slider(id = 'semestre',
                                                                                    min=1,
                                                                                    max=9,
                                                                                    marks={i: '{}+'.format(i) if i == 9 else str(i) for i in range(1, 9)},
                                                                                    value=1
                                                                                    
                                                                                )],
                                                                style = {'width':width_input, 'margin-left':'auto', 'margin-right':'auto'}
                                                        ),
                                                        html.P('Selecciona el número de semestres que has cursado.', style = {'color':color_footer,'margin-top':10}),
                                                        
                                                        html.H6('Elige los cursos a inscribir:', style = {'margin-top':margen,'color':color_letra}),
                                                        dcc.Dropdown(id = 'curso',
                                                            options=[
                                                                {'label': 'Python from Zero to Hero', 'value': 'Python-zh'},
                                                                {'label': 'Ingeniería de Datos con Python', 'value': 'Ingenieria-datos'},
                                                                #{'label': 'Pandas para ciencia de datos', 'value': 'Pandas-ciencia'},
                                                                {'label': 'MATLAB', 'value': 'Matlab'},
                                                                {'label': 'Python from Hero to God', 'value': 'Python-hg'},
                                                                {'label': 'Criptografía Aplicada en C++', 'value': 'Criptografia'},
                                                                {'label': 'Wolfram Mathematica', 'value': 'Wolfram'},
                                                                #{'label': 'Machine Learning', 'value': 'Mac', 'disabled': True}
                                                            ],
                                                            value='',
                                                            multi = True, 
                                                            searchable = False,
                                                            clearable = False,
                                                            style = {
                                                                'width': width_input,
                                                                'margin-left':'auto',
                                                                'margin-right':'auto'
                                                            }, placeholder = 'Cursos'
                                                        ),
                                                    
                                                        html.Div(id = 'elegir_horario'),
                                                        #html.P('Por el momento sólo puedes elegir un curso.', style = {'color':color_footer,'margin-top':10}),
                                                        html.Div(id = 'Python_accept', children = [dbc.Checklist(id = 'Accepted')]),
                                                    ], lg = 4),
                                                    dbc.Col([
                                                        html.Div(id = 'elegir_horario', style = {'margin-top':margen,'color':color_letra}),
                                                        html.H6('Escribe tus objetivos en el curso: ', style = {'margin-top':margen,'color':color_letra}),
                                                        #dcc.Input(id = 'objetivo',value='', type='text', style ={'width':'auto','width': 300, 'height':100}),
                                                        dbc.Textarea( id = 'objetivo',
                                                            placeholder='Se considerará si se excede el límite de cupo',
                                                            value='',
                                                            style ={'width':'auto','width': width_input, 'height':100, 'margin-left':'auto','margin-right':'auto'}
                                                        ),
                                                    ], lg = 4)  
                                                ])
                                                ],
                                                style = {'width':'100%','margin-left':'auto','margin-right':'auto', 'text-align': 'center'}
                                            
                                            ),
                                            html.Div(children = [
                                                dcc.Loading(
                                                        id="loading-1",
                                                        type="default",
                                                        children=html.P(id='Confirmacion'),#, style = {'color':'#db0000', 'padding':10}
                                                        color = '#7b1448'
                                                    )
                                            ],style = {'margin-left':'auto','margin-right':'auto', 'text-align': 'center', 'margin-top':20}),
                                            html.Div(children = [ 
                                                        dcc.Link( id = 'go_link', children = [
                                                            dbc.Button("Enviar", id='go', n_clicks=0, color="danger", className="mr-1")
                                                        ], href = '')
                                                ],
                                                style = {'width':'auto','margin-left':'auto','margin-right':'auto', 'text-align': 'center', 'margin-top':margen}
                                                ),
                                            
                                            # html.Div(children = [ 
                                                        
                                            #             dbc.Button('Limpiar', id='clean', n_clicks=0, outline=True, color="warning", className="mr-1")
                                            #     ],
                                            #     style = {'width':160,'margin-left':'auto','margin-right':'auto', 'text-align': 'center', 'margin-top':10}
                                            #     ),
                                            
                                            
                                            html.Div(children = [
                                                html.Footer(children = [ 
                                                    '*Al enviar tus datos aceptas su uso para confirmar su veracidad.',
                                                ],style = {'margin-left':'auto','margin-right':'auto', 'text-align': 'center','padding-bottom':20,'color':color_footer} ),
                                                
                                                    
                                            ], style = {'margin-top': 25})
                                            
                                            
                                                    
                                                    
                                                
                                            
                                            
                                            #html.P(html.A(dbc.Button("Unéte a Discord", color="primary"), href = "https://discord.gg/JxS59BFBu3",target="_blank" ), className="lead"),
                                        ], style = {"padding":"20px", "padding-top":20, "padding-bottom":5, "background-color":color_fondo}),
                                        
                                        
            ]
    else:
        #print(ide)
        return [html.Div([
                                            html.H1("Convocatoria 2021-2", className="display-3" , style ={"font-size":"3rem", "color":color_letra}, ),
                                            html.P(
                                                "Llena el siguiente formulario y espera una confirmación por e-mail",style = {"color":color_letra},
                                                className="lead",
                                            ),
                                        # html.Div(
                                        #         children = [
                                        #             html.Img (src="https://fotos.subefotos.com/b8055f292fdcc96840cc8cc172f6ab94o.png", 
                                        #                 style = {"margin-bottom":0,'min-width':450,"display":"block","width": '70%', "height": "auto", "margin-left": "auto", "margin-right": "auto", "margin-top": 30,"text-align":"center"})
                                        #         ] 
                                        #     ),
                                            dbc.Row([
                                                dbc.Col(html.Img (src='https://fotos.subefotos.com/dee1790fc6bec5718d06ec4c8d80ee71o.png', style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6),
                                                dbc.Col(html.Img (src='https://fotos.subefotos.com/673fd6a8b257776bc02619ac941b0783o.png', style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6),
                                                dbc.Col(html.Img (src='https://fotos.subefotos.com/8ad0901fd4fa9dbb648e720c3520b701o.png', style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6),
                                                dbc.Col(html.Img (src='https://fotos.subefotos.com/2eb394d174d94e6c0aff2a8f15cd7d42o.png', style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6),
                                                dbc.Col(html.Img (src='https://fotos.subefotos.com/a91e42ffd6b2dd249ecb4df0bb1c234do.png', style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6),
                                                dbc.Col(html.Img (src='https://fotos.subefotos.com/48b519d4b7109cb58d21dfceb259d54bo.png', style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6),
                                                #dbc.Col(html.Img (src='https://fotos.subefotos.com/dee1790fc6bec5718d06ec4c8d80ee71o.png'))
                                            ], justify = 'center'),
                                            html.Div(
                                            children =[ 
                                                    html.H6('Tu ID anterior es:  ', style = {'margin-top':margen,'color':color_letra}),
                                                        #dcc.Input(id = 'name',value='', type='text', style ={'width':'auto','width': 300}, placeholder = 'Empieza por tus nombres'),
                                                    html.Div([
                                                            dbc.Row([
                                                            dbc.Col([
                                                                dbc.Input(id = 'id_anterior',value=ide, disabled = True, type='text', style ={'width':'100%', 'margin-left':'auto','margin-right':'auto'}, placeholder = 'Puedes encontarlo en tu correo'),
                                                            ], width = 12),
                                                            # dbc.Col([
                                                            #     dbc.Button('Ir')
                                                            # ], width = 2)
                                                        ], no_gutters=True,),
                                                    ], style = {'width':300, 'margin-left':'auto','margin-right':'auto'}),
                                                        #html.P('Si no has tomado cursos anteriores, ignóralo.', style = {'color':color_footer,'margin-top':10}),
                                                dbc.Row([
                                                    dbc.Col([
                                                        #html.Div('Horarios sujetos a cupo, si se excede el primer horario mostrado se abrirá el otro.', style = {'font-size':'0.7em','color':color_letra}),
                                                        html.H6('Ingresa tu nombre completo: ', style = {'margin-top':margen,'color':color_letra}),
                                                        #dcc.Input(id = 'name',value='', type='text', style ={'width':'auto','width': 300}, placeholder = 'Empieza por tus nombres'),
                                                        dbc.Input(id = 'name',value=nombre, disabled = True, type='text', style ={'width':width_input, 'margin-left':'auto','margin-right':'auto'}, placeholder = 'Empieza por tus nombres'),
                                                        
                                                        html.H6('Ingresa tu número de boleta: ', style = {'margin-top':margen,'color':color_letra}),
                                                        #dcc.Input(id = 'boleta',value='', type='number', style ={'width':'auto','width': 300}),
                                                        dbc.Input(id = 'boleta',value=boleta, disabled = True, type='number', style ={'width': width_input, 'margin-left':'auto','margin-right':'auto'}),

                                                        html.H6('Ingresa tu correo institucional: ', style = {'margin-top':margen,'color':color_letra}),
                                                        #dcc.Input(id = 'correo',value='', type='email', style ={'width':'auto','width': 300}, placeholder = 'nombre@alumno.ipn.mx'),
                                                        dbc.Input(id = 'correo',value=correo, type='email', style ={'width': width_input, 'margin-left':'auto','margin-right':'auto'}, placeholder = 'nombre@alumno.ipn.mx'),
                                                        html.P('Si aún no tienes correo institucional ingresa otro correo.', style = {'color':color_footer,'margin-top':10}),
                                                    ], lg = 4),
                                                    dbc.Col([
                                                        html.H6('Elige tu carrera:', style = {'margin-top':margen,'color':color_letra}),

                                                        dcc.Dropdown(id = 'carrera',
                                                            options=[
                                                                {'label': 'Lic. en Matemática Algorítmica', 'value': 'Mat'},
                                                                {'label': 'Lic. en Física y Matemáticas', 'value': 'Lic'},
                                                                {'label': 'Ingeniería Matemática', 'value': 'Ing'},
                                                            
                                                            ],
                                                            value=carrera,
                                                            multi = False, 
                                                            searchable = False,
                                                            clearable = False,
                                                            style = {
                                                                'width': width_input,
                                                                'margin-left':'auto',
                                                                'margin-right':'auto'
                                                            }, placeholder = 'Carreras'
                                                        ),
                                                        html.H6('Elige tu semestre:', style = {'margin-top':margen,'color':color_letra}),
                                                        html.Div( children = [
                                                                                dcc.Slider(id = 'semestre',
                                                                                    min=1,
                                                                                    max=9,
                                                                                    marks={i: '{}+'.format(i) if i == 9 else str(i) for i in range(1, 9)},
                                                                                    value=semestre
                                                                                    
                                                                                )],
                                                                style = {'width':width_input, 'margin-left':'auto', 'margin-right':'auto'}
                                                        ),
                                                        html.P('Selecciona el número de semestres que has cursado.', style = {'color':color_footer,'margin-top':10}),
                                                        
                                                        html.H6('Elige los cursos a inscribir:', style = {'margin-top':margen,'color':color_letra}),
                                                        dcc.Dropdown(id = 'curso',
                                                            options=[
                                                                {'label': 'Python from zero to hero', 'value': 'Python-zh'},
                                                                {'label': 'Ingeniería de datos con Python', 'value': 'Ingenieria-datos'},
                                                                #{'label': 'Pandas para ciencia de datos', 'value': 'Pandas-ciencia'},
                                                                {'label': 'MATLAB', 'value': 'Matlab'},
                                                                {'label': 'Python from Hero to God', 'value': 'Python-hg'},
                                                                {'label': 'Criptografía Aplicada en C++', 'value': 'Criptografia'},
                                                                {'label': 'Wolfram Mathematica', 'value': 'Wolfram'},
                                                                #{'label': 'Machine Learning', 'value': 'Mac', 'disabled': True}
                                                            ],
                                                            value='',
                                                            multi = True, 
                                                            searchable = False,
                                                            clearable = False,
                                                            style = {
                                                                'width': width_input,
                                                                'margin-left':'auto',
                                                                'margin-right':'auto'
                                                            }, placeholder = 'Cursos'
                                                        ),
                                                    
                                                        html.Div(id = 'elegir_horario'),
                                                        #html.P('Por el momento sólo puedes elegir un curso.', style = {'color':color_footer,'margin-top':10}),
                                                        html.Div(id = 'Python_accept', children = [dbc.Checklist(id = 'Accepted')]),
                                                    ], lg = 4),
                                                    dbc.Col([
                                                        html.Div(id = 'elegir_horario', style = {'margin-top':margen,'color':color_letra}),
                                                        html.H6('Escribe tus objetivos en el curso: ', style = {'margin-top':margen,'color':color_letra}),
                                                        #dcc.Input(id = 'objetivo',value='', type='text', style ={'width':'auto','width': 300, 'height':100}),
                                                        dbc.Textarea( id = 'objetivo',
                                                            placeholder='Se considerará si se excede el límite de cupo',
                                                            value='',
                                                            style ={'width':'auto','width': width_input, 'height':100, 'margin-left':'auto','margin-right':'auto'}
                                                        ),
                                                    ], lg = 4)  
                                                ])
                                                ],
                                                style = {'width':'100%','margin-left':'auto','margin-right':'auto', 'text-align': 'center'}
                                            
                                            ),
                                            html.Div(children = [
                                                dcc.Loading(
                                                        id="loading-1",
                                                        type="default",
                                                        children=html.P(id='Confirmacion'),#, style = {'color':'#db0000', 'padding':10}
                                                        color = '#7b1448'
                                                    )
                                            ],style = {'margin-left':'auto','margin-right':'auto', 'text-align': 'center', 'margin-top':20}),
                                            html.Div(children = [ 
                                                        dcc.Link( id = 'go_link', children = [
                                                            dbc.Button("Enviar", id='go', n_clicks=0, color="danger", className="mr-1")
                                                        ], href = '')
                                                ],
                                                style = {'width':'auto','margin-left':'auto','margin-right':'auto', 'text-align': 'center', 'margin-top':margen}
                                                ),
                                            
                                            # html.Div(children = [ 
                                                        
                                            #             dbc.Button('Limpiar', id='clean', n_clicks=0, outline=True, color="warning", className="mr-1")
                                            #     ],
                                            #     style = {'width':160,'margin-left':'auto','margin-right':'auto', 'text-align': 'center', 'margin-top':10}
                                            #     ),
                                            
                                            
                                            html.Div(children = [
                                                html.Footer(children = [ 
                                                    '*Al enviar tus datos aceptas su uso para confirmar su veracidad.',
                                                ],style = {'margin-left':'auto','margin-right':'auto', 'text-align': 'center','padding-bottom':20,'color':color_footer} ),
                                                
                                                    
                                            ], style = {'margin-top': 25})
                                            
                                            
                                                    
                                                    
                                                
                                            
                                            
                                            #html.P(html.A(dbc.Button("Unéte a Discord", color="primary"), href = "https://discord.gg/JxS59BFBu3",target="_blank" ), className="lead"),
                                        ], style = {"padding":"20px", "padding-top":20, "padding-bottom":5, "background-color":color_fondo}),
                                        
                                        
            ]