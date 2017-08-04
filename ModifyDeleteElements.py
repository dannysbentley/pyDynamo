import clr

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

elements = UnwrapElement(IN[0])

TransactionManager.Instance.EnsureInTransaction(doc)

for e in elements:
    doc.Delete(e.Id)

TransactionManager.Instance.TransactionTaskDone()

OUT = "done"