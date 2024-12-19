def similarity_module(data, method, ids, exclude_keys):

    # Using nested functions
    def preprocess_data(record):
        return {k: float(v) for k, v in record.items() if k not in exclude_keys and v.replace('.', '', 1).isdigit()}

    def cosine_similarity(features ,id1, id2):
        list1 = list(preprocess_data(features[id1]).values()) 
        list2 = list(preprocess_data(features[id2]).values())
       
        dot_product = sum(a * b for a, b in zip(list1, list2))
        magnitude_a = sum(a ** 2 for a in list1) ** 0.5
        magnitude_b = sum(b ** 2 for b in list2) ** 0.5
        
        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0
        else: 
            return dot_product / (magnitude_a * magnitude_b)
     
    def euclidean_distance(features ,id1, id2):
        list1 = list(preprocess_data(features[id1]).values()) 
        list2 = list(preprocess_data(features[id2]).values())
        return  sum((a - b) ** 2 for a, b in zip(list1, list2)) ** 0.5
    
    def euclidean_similarity(features ,id1, id2):
        return 1 / (1 + euclidean_distance(features, id1, id2))
    
    def jaccard_similarity(features ,id1, id2):
        list1 = list(preprocess_data(features[id1]).values())
        list2 = list(preprocess_data(features[id2]).values())
        
        intersection = len(set(list1) & set(list2))
        union = len(set(list1) | set(list2))
        return intersection / union if union != 0 else 0
        
    def manhattan_distance(features ,id1, id2):
        list1 = list(preprocess_data(features[id1]).values())
        list2 = list(preprocess_data(features[id2]).values())
        return sum(abs(a - b) for a, b in zip(list1, list2))
    
    def manhattan_similarity(features ,id1, id2):
        return 1 / (1 + manhattan_distance(features, id1, id2))
 
    def pearson_similarity(features ,id1, id2):
        list1 = list(preprocess_data(features[id1]).values())
        list2 = list(preprocess_data(features[id2]).values())
    
        mean_x = sum(list1) / len(list1)
        mean_y = sum(list2) / len(list2)
        std_dev_x = (sum((x - mean_x) ** 2 for x in list1) / len(list1)) ** 0.5
        std_dev_y = (sum((y - mean_y) ** 2 for y in list2) / len(list2)) ** 0.5
        covariance = sum((x - mean_x) * (y - mean_y) for x, y in zip(list1, list2)) / len(list1)
        if std_dev_x == 0 or std_dev_y == 0:
            return 0
        return covariance / (std_dev_x * std_dev_y)
        
    methods = {
        'cosine': cosine_similarity,
        'euclidean': euclidean_similarity,
        'jaccard': jaccard_similarity,
        'manhattan': manhattan_similarity,
        'pearson': pearson_similarity,
    }

    method = str(method).strip().lower()
    similarity_function = methods.get(method)
    
    if similarity_function: 
        return similarity_function(data, ids[0], ids[1])
    else:
        raise ValueError(f"Unknown similarity method: {method}")