using Microsoft.Win32;
using OperatorMonitor.Interstructures;
using System.Windows.Input;
using OperatorMonitor.Models;
using System.Diagnostics;

namespace OperatorMonitor.ViewModels
{
    internal class MonitorWindowVM: ViewModel
    {
        VideoClumpModel VideoModel = new();
        public ICommand OpenFileCMD { get; }
        bool CanOpenFile(object p) => true;
        void OnOpenFile(object o)
        {
            OpenFileDialog op = new OpenFileDialog();
            op.Title = "Выбирете видеофайлы";
            op.Multiselect = true;
            op.Filter = "Видео|*.mp4";
            if (op.ShowDialog() == true)
            {
                foreach(string fileName in op.FileNames)
                {
                    Trace.WriteLine($"Файл: {fileName}");
                }
            }
        }

        public MonitorWindowVM()
        {
            OpenFileCMD = new LambdaCommand(OnOpenFile, CanOpenFile);
        }
    }
}
