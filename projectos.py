def analyze_memory_constraints(memory_data):
    """
    Analyzes memory constraints based on usage data.
    
    :param memory_data: DataFrame with memory usage data.
    """
    # Calculate average and peak memory usage
    average_usage = memory_data.groupby('node_id')['memory_used_gb'].mean()
    peak_usage = memory_data.groupby('node_id')['memory_used_gb'].max()
    
    # Identify nodes with high average or peak memory usage
    high_avg_usage_nodes = average_usage[average_usage > (0.8 * 256)].index.tolist()  # 80% of total memory
    high_peak_usage_nodes = peak_usage[peak_usage > (0.9 * 256)].index.tolist()  # 90% of total memory
    
    print(f"Nodes with high average memory usage: {high_avg_usage_nodes}")
    print(f"Nodes with high peak memory usage: {high_peak_usage_nodes}")
    
    # Visualization (optional)
    average_usage.plot(kind='bar', title='Average Memory Usage per Node')
    peak_usage.plot(kind='bar', color='red', title='Peak Memory Usage per Node')

# Analyze the simulated data
analyze_memory_constraints(memory_data)def analyze_memory_constraints(memory_data):
    """
    Analyzes memory constraints based on usage data.
    
    :param memory_data: DataFrame with memory usage data.
    """
    # Calculate average and peak memory usage
    average_usage = memory_data.groupby('node_id')['memory_used_gb'].mean()
    peak_usage = memory_data.groupby('node_id')['memory_used_gb'].max()
    
    # Identify nodes with high average or peak memory usage
    high_avg_usage_nodes = average_usage[average_usage > (0.8 * 256)].index.tolist()  # 80% of total memory
    high_peak_usage_nodes = peak_usage[peak_usage > (0.9 * 256)].index.tolist()  # 90% of total memory
    
    print(f"Nodes with high average memory usage: {high_avg_usage_nodes}")
    print(f"Nodes with high peak memory usage: {high_peak_usage_nodes}")
    
    # Visualization (optional)
    average_usage.plot(kind='bar', title='Average Memory Usage per Node')
    peak_usage.plot(kind='bar', color='red', title='Peak Memory Usage per Node')

# Analyze the simulated data
analyze_memory_constraints(memory_data)