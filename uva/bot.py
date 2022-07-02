from tkinter import messagebox
from botcity.web import WebBot, Browser

# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
from botcity.maestro import *


class Bot(WebBot):
    def action(self, execution=None):
        # Configure whether or not to run on headless mode
        place = "rio de janeiro"

        if execution:
            place = execution.parameters["municipio"]
        self.headless = False

        # Uncomment to change the default Browser to Firefox
        # self.browser = Browser.FIREFOX

        # Uncomment to set the WebDriver path
        self.driver_path = r"C:\Users\mauro.morais\OneDrive - T2C CONSULTORIA LTDA\Documentos\Python\Projetos\extracaoSiteIBGE\uva\infra\chromedriver.exe"

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        self.browse("https://cidades.ibge.gov.br/")
        self.find_element("body > app > shell > header > busca > div > input").click()
        self.type_keys('{}\n'.format(place))
        self.wait(5000)
        self.execute_javascript("document.querySelector('body > app > shell > header > busca > div > div.busca__auto-completar > div > div:nth-child(1) > a').click()")
        self.wait(10000)
        populacao = self.find_element("#detalhes > panorama-temas > panorama-painel:nth-child(3) > div > div.painel__indicadores > panorama-card:nth-child(1) > div > div.indicador__valor").text
        print(populacao)
        messagebox.showinfo(title='teste',  message=populacao)
        self.wait(10000)
        # Uncomment to mark this task as finished on BotMaestro

        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

        # Stop the browser and clean up
        self.stop_browser()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
