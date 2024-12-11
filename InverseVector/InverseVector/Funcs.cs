using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace InverseVector
{
    internal class Funcs
    {
        static public List<int> PermToInv(List<int> perm)
        {
            List<int> inv = new List<int>();
            for (int i = 0; i < perm.Count; i++)
                inv.Add(0);
            for (int i = 1; i < perm.Count; i++)
                for (int j = 0; j < i; j++)
                    if (perm[j] > perm[i])
                        inv[i]++;
            return inv;
        }
        static public List<int> InvToPerm(List<int> inv)
        {
            List<int> perm = new List<int>();
            for (int i = 0; i < inv.Count; i++)
                perm.Add(0);
            List<int> alphabet = new List<int>();
            for (int i = 1; i <= inv.Count; i++)
                alphabet.Add(i);
            for (int i = inv.Count - 1; i >= 0; i--)
            {
                perm[i] = alphabet[alphabet.Count - 1 - inv[i]];
                alphabet.Remove(alphabet[alphabet.Count - 1 - inv[i]]);
            }
            return perm;
        }
        static public string ListToString(List<int> list)
        {
            string line = "";
            for (int i = 0; i < list.Count; i++)
                line += list[i].ToString() + " ";
            return line;
        }
        static public string ListToPermString(List<int> list)
        {
            string line = "";
            string topLine = "";
            for (int i = 0; i < list.Count; i++)
            {
                topLine += (i + 1).ToString() + " ";
                line += list[i].ToString() + " ";
            }
            return topLine + "\n" + line;
        }
    }
}
