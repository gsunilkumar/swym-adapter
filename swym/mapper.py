
class Mapper(object):
    @staticmethod
    def Transform(source, target, lookup):
        sourceKeys = source.keys()
        lookupKeys = lookup.keys()

        removeReverseKey = True # make it mapper configuration
        for k in lookup:
            targetValue = None
            if k in lookupKeys and lookup[k] in sourceKeys:
                targetValue = source[lookup[k]]
                if removeReverseKey and lookup[k] in target.keys():
                    del target[lookup[k]]

            target[k] = targetValue