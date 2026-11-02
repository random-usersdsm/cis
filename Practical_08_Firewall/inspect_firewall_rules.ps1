# Read-only: lists firewall rules; makes no configuration changes.
Get-NetFirewallRule | Select-Object DisplayName, Enabled, Direction, Action, Profile |
    Format-Table -AutoSize
