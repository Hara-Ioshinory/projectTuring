using System.Collections.ObjectModel;
using Microsoft.Win32;
using System.Windows;
using Newtonsoft.Json;

namespace OperatorMonitor
{
    public partial class MonitorWindow : Window
    {
        ObservableCollection<string> LoadedFiles = new();
        ObservableCollection<string> Events = new();

        public MonitorWindow()
        {
            InitializeComponent();
            MaxHeight = SystemParameters.MaximizedPrimaryScreenHeight;
            MaxWidth = SystemParameters.MaximizedPrimaryScreenWidth;
            EventsListView.ItemsSource = Events;
            FileListView.ItemsSource = LoadedFiles;
        }

        private void OpenFile(object sender, RoutedEventArgs e)
        {
            OpenFileDialog op = new OpenFileDialog();
            op.Title = "Выбирете видеофайлы";
            op.Multiselect = true;
            op.Filter = "Видео|*.mp4";
            if (op.ShowDialog() == true)
            {
                foreach (string fileName in op.FileNames)
                {
                    if(!LoadedFiles.Contains(fileName.ToString()))
                        LoadedFiles.Add(fileName.ToString());
                }
            }
        }

        private void AddEvent(object sender, RoutedEventArgs e)
        {
            if(NewEventName.Text.Length != 0)
            {
                Events.Add(NewEventName.Text);
                NewEventName.Clear();
            }
        }
    }
}
