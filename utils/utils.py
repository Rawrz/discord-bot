
def strip_global_mentions(message, ctx=None):
    if ctx:
        perms = ctx.message.channel.permissions_for(ctx.message.author)
        if perms.mention_everyone:
            return message
    remove_everyone = re.compile(re.escape("@everyone"), re.IGNORECASE)
    remove_here = re.compile(re.escape("@here"), re.IGNORECASE)
    message = remove_everyone.sub("everyone", message)
    message = remove_here.sub("here", message)
    return message