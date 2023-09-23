using System.Windows;

namespace OperatorMonitor
{
    public partial class MonitorWindow : Window
    {
        public MonitorWindow()
        {
            InitializeComponent();
            MaxHeight = SystemParameters.MaximizedPrimaryScreenHeight;
            MaxWidth = SystemParameters.MaximizedPrimaryScreenWidth;
        }
    }
}
