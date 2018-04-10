from cursos.models import Instrutor, Categoria, Curso, Unidade, Atividade, VideoAula, MaterialComplementar

instrutor = Instrutor(nome='Paulo Silveira', contato='@paulo_caelum', resumo='Instrutor e desenvolvedor na Caelum e no Alura, fundador do GUJ.com.br e um dos criadores do VRaptor.')
instrutor.save()

categoria = Categoria(nome='Programação')
categoria.save()

curso = Curso(titulo='Java: Dominando as Collections', categoria=categoria, instrutor=instrutor, palavras_chave='teste teste123') 
curso.save()

unidade1 = Unidade(titulo='Trabalhando com ArrayList', curso=curso)
unidade1.save()

unidade2 = Unidade(titulo='Lista de objetos', curso=curso)
unidade2.save()

unidade3 = Unidade(titulo='Relacionamentos com coleções', curso=curso)
unidade3.save()

atividade = Atividade(titulo='Trabalhando com ArrayList', unidade=unidade1)
atividade.save()

video_aula_1 = VideoAula(uri='http://youtube.com', atividade=atividade)
video_aula_1.save()

material_complementar_1 = MaterialComplementar(uri='ftp://servidor.ftp.com/material_complementar_1', atividade=atividade)
material_complementar_1.save()