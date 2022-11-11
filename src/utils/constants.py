class Constant:
    QUOTE_API = 'https://zenquotes.io/api/random'
    INVALID_QUERY_ARGUMENT = "invalid query, $todo must have at least two argument"
    INVALID_QUERY_UPDATE_ARGS = "Invalid query, format update should be: `$query update {id} [done|undone]`"
    INVALID_QUERY_SELECT_ARGS = "Invalid query, format select should be: `$query select {id}`"
    INVALID_QUERY_DELETE_ARGS = "Invalid query, format delete should be: `$query delete {id}`"
    INVALID_QUERY_CLEAR_ARGS = "Invalid query, format clear should only be: `$query clear`"
    EMPTY_QUERY_VIEW = "Your todo list is empty..."
    DEFAULT_ERROR_MESSAGE = "Something went wrong..."
    SUCCESSFUL_QUERY_CLEAR = "Todo tasks have been successfully cleared"
