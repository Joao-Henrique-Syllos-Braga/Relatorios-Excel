using System;
using System.Diagnostics;
using System.Windows.Forms;

class Program
{
    [STAThread]
    static void Main()
    {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);

        Form form = new Form
        {
            Text = "Explorador de Arquivos",
            Width = 400,
            Height = 300
        };

        // Botão para abrir arquivo
        Button button = new Button
        {
            Text = "Abrir Arquivo",
            Width = 150,
            Height = 40,
            Location = new System.Drawing.Point(120, 80)
        };
        form.Controls.Add(button);

        // Botão para selecionar local
        Button localSel = new Button
        {
            Text = "Selecionar Local",
            Width = 150,
            Height = 40,
            Location = new System.Drawing.Point(120, 130)
        };
        form.Controls.Add(localSel);

        // Botão para processar arquivo
        Button processar = new Button
        {
            Text = "Processar Arquivo",
            Width = 150,
            Height = 40,
            Location = new System.Drawing.Point(120, 180)
        };
        form.Controls.Add(processar);

        // Variáveis para armazenar informações do arquivo e do local
        string arquivo = null;
        string local = null;

        // Evento para selecionar o arquivo
        button.Click += (sender, e) =>
        {
            OpenFileDialog openFileDialog = new OpenFileDialog
            {
                Title = "Selecione um Arquivo",
                Filter = "Arquivos Excel (*.xlsx)|*.xlsx"
            };

            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                arquivo = openFileDialog.FileName;
                MessageBox.Show($"Arquivo selecionado: {arquivo}");
            }
        };

        // Evento para selecionar o local
        localSel.Click += (sender, e) =>
        {
            using (FolderBrowserDialog folderDialog = new FolderBrowserDialog())
            {
                folderDialog.Description = "Selecione o local para salvar o arquivo";
                if (folderDialog.ShowDialog() == DialogResult.OK)
                {
                    local = folderDialog.SelectedPath;
                    MessageBox.Show($"Local selecionado: {local}");
                }
            }
        };

        // Evento para processar o arquivo
        processar.Click += (sender, e) =>
        {
            if (string.IsNullOrEmpty(arquivo))
            {
                MessageBox.Show("Por favor, selecione um arquivo antes de processar!");
                return;
            }

            if (string.IsNullOrEmpty(local))
            {
                MessageBox.Show("Por favor, selecione um local antes de processar!");
                return;
            }

            ProcessarArquivo(arquivo, local);
        };

        // Método para processar o arquivo usando Python
        static void ProcessarArquivo(string arquivo, string local)
        {
            try
            {
                ProcessStartInfo start = new ProcessStartInfo
                {
                    FileName = "python",
                    Arguments = $"process.py \"{arquivo}\" \"{local}\"",
                    RedirectStandardOutput = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                using (Process process = Process.Start(start))
                {
                    string resultado = process.StandardOutput.ReadToEnd();
                    process.WaitForExit();
                    MessageBox.Show($"Resultado do Python: {resultado}");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Erro ao executar o script Python: {ex.Message}");
            }
        }

        Application.Run(form);
    }
}
